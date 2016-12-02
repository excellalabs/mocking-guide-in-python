import requests

dummy_api = 'http://httpbin.org/post'

PEETA = 'peeta'
GALE = 'gale'
HAYMITCH = 'haymitch'
SNOW = 'snow'
COIN = 'coin'


class Jay():

    friends = [PEETA, GALE, HAYMITCH]

    def hug(self):
        requests.post(dummy_api, json={'grab_tissues': True})

    def encounter(self, character):
        if character.lower() in self.friends:
            self.hug()
        return "%s encountered" % character
