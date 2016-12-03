import random


class MockingBirdDontSingException(Exception):

    def __init__(self):
        Exception.__init__(self, "Mama's gonna buy you a diamond ring.")


class Bird():

    def sing(self):

        if random.randint(1, 2) == 1:
            raise MockingBirdDontSingException()
        else:
            return "chirp chirp"
