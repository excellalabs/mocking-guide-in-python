import requests

dummy_api = 'http://httpbin.org/post'


class Jay():

    friends = ['peeta', 'gale', 'haymitch']

    def hug(self, friend):
        requests.post(dummy_api, json={'friend': friend,
                                       'grab_tissues': True})

    def encounter(self, character):
        if character.lower() in self.friends:
            self.hug(character)
        return "%s encountered" % character
