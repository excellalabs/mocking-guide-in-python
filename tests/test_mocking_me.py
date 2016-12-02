from mocking.me import via_gif
from unittest import TestCase

try:
    from mock import patch
except ImportError:
    from unittest.mock import patch

# What's missing:
#   Testing an external API can be done without mocking, but it only
#   works if the API is available.  In addition, tests may be slow and
#   running tests too often may exceed API query thresholds.
#
#   Update the tests so that they do not query the external API


class TestMockingMe(TestCase):

    # TODO patch here
    def test_mocking_me_via_gif_when_resp_200_then_get_gif(self):
        # Arrange
        name = 'First Last'
        # TODO set patch object's return value(s)

        # Act
        result = via_gif(name)

        # Assert
        assert result == "gif content"

    # TODO patch here
    def test_mocking_me_via_gif_when_resp_not_200_then_Exception(self):
        # Arrange
        name = 'First Last'
        # TODO set patch object's return value(s)

        # Act
        # Assert
        self.assertRaises(Exception, via_gif, name)
