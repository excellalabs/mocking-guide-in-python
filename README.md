# Mocking Guide (in Python)

Python provides a mock library that is essential for writing unit tests, but can be intimidating to folks new to mocking.

This is a hands-on guide for those who are new to the concept of test mocks, also known as 'stubs', 'fakes', and 'test doubles'.

### How to install

Clone this repo

```
git clone https://github.com/excellalabs/mocking-guide-in-python
cd mocking-guide-in-python
```

Install the dependencies

```
virtualenv env
. env/bin/activate
pip install -r requirements.txt
```

# The Exercises

This repo has three modules with partially written (and failing) tests.  Execute the following command to run the failing tests:

```
pytest
```

You'll notice that some of the tests take a long time to run.  This is because they're hitting an external API that takes a while to respond.  Let's fix that first...

### Exercise 1: Mocking Me

Review the code for `mocking/me.py`, and the partially completed `tests/test_mocking_me.py`.

Notice the code for `via_gif` hits an external API.  How do we test that the function handles response codes correctly? Do the tests run quickly?

#### Why do we need mocks?

Unit tests should test the smallest testable part of an application. Tests that hit outside code or APIs are integration tests, not unit tests.

Mocking is a mechanism to remove outside dependencies so you can create proper unit tests.

 * Run tests even if the API is not available
 * Create scenarios that are hard to reproduce with the real interface
 * Tests run quickly even if the real interface is slow

#### What you need to do:

 * Open the mock [documentation](https://docs.python.org/dev/library/unittest.mock.html)
   * Read about library's `patch` decorator
   * Read about the Mock object's `return_value` capability
 * Use `patch` to replace requests's `post` function with a dummy Mock object
   * In the first test, get the `via_gif` function to return "gif content"
     * Hint: `return_value` is pretty flexible, there is no need to create a "response" object to house the `_content` element. You can simply do `mock_object.return_value._content = 'gif content'`
   * In the second test, get the `via_gif` function to throw an Exception

#### How to know you're done:

 * You're done when the following command results in two passing tests:

```
pytest tests/test_mocking_me.py
```

### Exercise 2: Mocking Bird

Review the code for `mocking/bird.py`, and the partially completed `tests/test_mocking_bird.py`.

The tests actually pass... sometimes... try running the tests 10 times, and see how many pass

```shell
for i in {1..10}; do pytest tests/test_mocking_bird.py ; done
```

#### Why do we need mocks?

 * Create predictable scenarios for interfaces that have unpredictable results

#### What you need to do:

 * Recall what you learned about `patch` and `return_value` in the first exercise
 * Use `patch` to mock `randomint` in the two tests
   * In the first test, ensure `sing()` always returns "chirp chirp"
   * In the second test, ensure `sing()` always throws an error

#### How to know you're done:

 * You're done when the following command results in two passing tests every time:

```shell
for i in {1..10}; do pytest tests/test_mocking_bird.py ; done
```

### Exercise 3: Mocking Jay

Review the code for `mocking/jay.py`, and the partially completed `tests/test_mocking_jay.py`.

How do we test if `hug()` gets called when we expect it to?

#### Why do we need mocks?

 * Test interactions with interfaces that have no return value

#### What you need to do:

 * Recall what you learned about `patch` and `return_value` in the previous exercises
 * Read about the Mock class
   * attributes like `called` and `call_count`
   * assertion helpers like `assert_called_once_with` and `assert_has_calls`
 * Use `patch` to mock `hug` in the two tests
 * Use Mock's attribute `called` to fix the tests
   * In the first test, ensure `hug` is executed
   * In the first test, ensure `hug` is NOT executed
 * Bonus: Get the tests passing with `assert_called_once_with`

#### How to know you're done:

 * You're done when all tests pass

```
pytest
```


# Web Demo

The Flask web demo is not required to complete all the exercises, but it does give a visual feel for what the functions do.

To run the web demo:

```
pip install -r webdemo/requirements.txt
python -m webdemo.app
```

The following link should work in your browser: http://localhost:5000
