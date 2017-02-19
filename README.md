# Mocking Guide (in Python)

Python provides a mock library that is essential for writing unit tests, but can be intimidating to folks new to mocking.

This is a hands-on guide for those who are new to testing with mocks, also known as 'stubs', 'fakes', and 'test doubles'.

### Before you begin

This guide assumes a general knowledge about the Python programming language.

To complete the exercises, you will need the following software installed on your system:

* Python 2 or 3
* virtualenv
* pip

The commands provided in this guide are targeted to folks using a bash environment (Mac, Linux).  You will likely need to perform different steps on a Windows machine.

### How to install this guide

First, clone this repo

```
git clone https://github.com/excellalabs/mocking-guide-in-python
cd mocking-guide-in-python
```

Then install the python dependencies in a virtual environment

```
virtualenv env
. env/bin/activate
pip install -r requirements.txt
```

# Demo Web App

A demo web app, written in Flask, provides example integrations with the code we cover in the three exercises. The demo is not required to complete the exercises.

To run the demo:

```
pip install -r demo/requirements.txt
python -m demo.app
```

The following link should work in your browser: [http://localhost:5000](http://localhost:5000)

# The Exercises

This repo has three modules with partially written (and failing) tests.  Execute the following command to run the failing tests:

```
pytest
```

You'll notice that some of the tests take a long time to run.  This is because they're hitting an external API that takes a while to respond.  Let's fix that first...

### Exercise 1: Mocking Bird

Review the code for `mocking/bird.py`, and the partially completed `tests/test_mocking_bird.py`.

The tests actually pass... sometimes... try running the tests 10 times, and see how many pass

```shell
# Linux/Mac shell command
for i in {1..10}; do pytest tests/test_mocking_bird.py ; done | grep seconds
```

#### Why do we need mocks?

 * Create predictable scenarios for interfaces that have unpredictable results

#### What you need to do:

 * Open the mock [documentation](https://docs.python.org/dev/library/unittest.mock.html)
   * Read about library's `patch` decorator
   * Read about the Mock object's `return_value` capability
 * Use `patch` to mock `randomint` in the two tests
   * In the first test, ensure `sing()` always returns "chirp chirp"
   * In the second test, ensure `sing()` always throws an error

#### How to know you're done:

 * You're done when the following command results in two passing tests every time:

```shell
# Linux/Mac shell command
for i in {1..10}; do pytest tests/test_mocking_bird.py ; done | grep seconds
```

### Exercise 2: Mocking Me

Review the code for `mocking/me.py`, and the partially completed `tests/test_mocking_me.py`.

Notice the code for `via_gif` hits an external API.  How do we test that the function handles response codes correctly? Do the tests run quickly?

#### Why do we need mocks?

Unit tests should test the smallest testable part of an application. Tests that hit outside code or APIs are integration tests, not unit tests.

Mocking is a mechanism to decouple outside dependencies, making it easy to create proper unit tests.

 * Run tests even if the API is not available
 * Create scenarios that are hard to reproduce with the real interface
 * Tests run quickly even if the real interface is slow

#### What you need to do:

 * Recall what you learned about `patch` and `return_value` in the first exercise
 * Use `patch` to replace requests's `post` function with a dummy Mock object
   * In the first test, get the `via_gif` function to return "gif content"
     * Hint: `return_value` is pretty flexible, there is no need to create a "response" object to house the `_content` element. You can simply do `mock_object.return_value._content = 'gif content'`
   * In the second test, get the `via_gif` function to throw an Exception

#### How to know you're done:

 * You're done when the following command results in two passing tests:

```
pytest tests/test_mocking_me.py
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

 * You're done when both tests confirm whether hug() was called or not, and the tests pass

```
pytest tests/test_mocking_jay.py
```

### Closing Out

At this point, ALL your tests should be passing.  Let's confirm by running all tests:

```
pytest
```
