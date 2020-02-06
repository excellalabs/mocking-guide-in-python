from mocking.jay import Jay
from unittest.mock import patch

# What's missing:
#     Test whether or not the 'hug' function was called while executing
#     'jay.encounter'. Unlike mocking.me and mocking.bird, we cannot rely
#     on mock object return values to facilitate our scenarios.


class TestMockingJay:

    # TODO patch here
    def test_mocking_jay_when_encounter_friend_then_hug(self):
        # Arrange
        jay = Jay()

        # Act
        jay.encounter('peeta')

        # Assert
        # TODO add assert confirming a hug occurred

    # TODO patch here
    def test_mocking_jay_when_encounter_non_friend_then_no_hug(self):
        # Arrange
        jay = Jay()

        # Act
        jay.encounter('snow')

        # Assert
        # TODO add assert confirming a hug did NOT occur
