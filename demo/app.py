#!/usr/bin/env python

from flask import Flask, send_file, render_template
import io
from mocking import me, jay, bird
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/mocking/<name>')
def api_mocking_me(name):
    try:
        gif = me.via_gif(name)
    except Exception:
        return 'Error: Unable to generate image'
    return send_file(io.BytesIO(gif),
                     attachment_filename='%s.gif' % name,
                     mimetype='image/gif')

@app.route('/mockingbird/sing')
def api_mocking_bird_sing():
    b = bird.Bird()
    try:
        result = b.sing()
    except bird.MockingBirdDontSingException:
        result = "This mocking bird don't sing"
    return result

@app.route('/mockingjay/encounter/<character>')
def api_mocking_jay(character):
    j = jay.Jay()
    return j.encounter(character)

if __name__ == '__main__':
    app.run()
