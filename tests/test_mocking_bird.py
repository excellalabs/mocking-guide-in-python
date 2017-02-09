from mocking.bird import Bird, DiamondRingException
from unittest import TestCase

try:
    from mock import patch
except ImportError:
    from unittest.mock import patch

# What's missing:
#     The first test passes sometimes, other times it fails. The second
#     test has the same problem!  Make is so that both tests ALWAYS pass.


class TestMockingBird(TestCase):

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
    def test_mocking_bird_when_dont_sing_then_get_diamond_ring_exception(self):
        # Arrange
        bird = Bird()
        # TODO set patch object's return value(s)

        # Act
        # Assert
        self.assertRaises(DiamondRingException, bird.sing)
