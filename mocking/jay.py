import requests

dummy_api = 'http://httpbin.org/post'


class Character():

    def __init__(self, name):
        self.name = name

PEETA = Character(name="Peeta")
GALE = Character(name="Gale")
HAYMITCH = Character(name="Haymitch")
SNOW = Character(name="Snow")
COIN = Character(name="Coin")


class Jay():

    friends = [PEETA, GALE, HAYMITCH]

    def hug(self):
        requests.post(dummy_api, json={'grab_tissues': True})

    def encounter(self, character):
        if character in self.friends:
            self.hug()
        return "%s encountered" % character.name
