# Mocking Guide (in Python)


Python provides a mock library that is essential for writing unit tests, but can be intimidating to folks new to mocking.

This is a guide for those who are new to the concept of test mocking, also known as 'stubbing'.

### How to install

Clone this repo

```shell
git clone https://github.com/excellalabs/mocking-guide-in-python
cd mocking-guide-in-python
```

Install the dependencies

```shell
virtualenv env
. env/bin/activate
pip install -r requirements.txt
```

# The Challenges

This repo has three modules with partially written (and failing) tests.  Run the following command to run the failing tests:

```shell
pytest
```

You'll notice that some of the tests take a long time to run.  This is because they're hitting an external API that takes a while to respond.  Let's fix that first...

### Challenge 1: Mocking Me

Review the code for `mocking/me.py`, and the partially completed `tests/test_mocking_me.py`.

#### Why do we need mocks?


 * What happens if the third party API is not available when running tests?
 * What happens if an API is really slow to create a result?

Unit tests should be fast, and not dependent on an external tool or class.  Those types of tests are integration tests, not unit tests.

#### What you need to do:

 * Read about mock's `patch` tool
 * Read about mock's `return_value` capability
 * Use `patch` to mock `requests.post` in the two tests
   * In the first test, get the `via_gif` function to return "gif content"
   * In the second test, get the `via_gif` function to throw an Exception

#### How to know you're done:

 * You're done when the following command results in two passing tests:

```shell
pytest tests/test_mocking_me.py
```

### Challenge 2: Mocking Bird

Review the code for `mocking/bird.py`, and the partially completed `tests/test_mocking_bird.py`.

#### Why do we need mocks?

 * What happens if the code we're integrating with has unpredictable results?

#### What you need to do:

 * Recall what you learned about `patch` and `return_value` in the first challenge
 * Use `patch` to mock `randomint` in the two tests
   * In the first test, ensure `sing()` always returns "chirp chirp"
   * In the second test, ensure `sing()` always throws an error

#### How to know you're done:

 * You're done when the following command results in two passing tests:

```shell
pytest tests/test_mocking_bird.py
```

### Challenge 3: Mocking Jay

Review the code for `mocking/jay.py`, and the partially completed `tests/test_mocking_jay.py`.

#### Why do we need mocks?

 * What happens if the code we're integrating with has no return value?

#### What you need to do:

 * Recall what you learned about `patch` and `return_value` in the first challenge
 * Read about mock's assertion tools (called, called_with_args, etc.)
 * Use `patch` to mock `hug` in the two tests
   * In the first test, ensure `hug` is executed
   * In the first test, ensure `hug` is not executed

#### How to know you're done:

 * You're done when all tests pass

```shell
pytest
```

