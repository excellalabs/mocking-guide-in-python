from mocking.bird import Bird, MockingBirdDontSingException
from unittest import TestCase

try:
    from mock import patch
except ImportError:
    from unittest.mock import patch

# What's missing:
#     The first test passes sometimes, other times it fails. The second
#     test has the same problem!  Make is so that both tests ALWAYS pass.


class TestMockingMe(TestCase):

    # TODO patch here
    def test_mocking_bird_when_sing_then_get_song(self):
        # Arrange
        bird = Bird()
        # TODO set patch object's return value(s)

        # Act
        result = bird.sing()

        # Assert
        assert result == "chirp chirp"

    # TODO patch here
    def test_mocking_bird_when_dont_sing_then_get_diamong_ring_exception(self):
        # Arrange
        bird = Bird()
        # TODO set patch object's return value(s)

        # Act
        # Assert
        self.assertRaises(MockingBirdDontSingException, bird.sing)
