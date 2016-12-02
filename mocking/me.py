import requests

gif_api_endpoint = 'https://gif-it-to-me-baby.herokuapp.com'


def via_gif(name):
    args = {'search': 'nelson haha', 'text': name}
    resp = requests.post(gif_api_endpoint, json=args)
    if resp.code != 200:
        raise Exception("Unable to get gif")
    return resp._content
