import os
import json
from flask import Flask
from flask import render_template, url_for

JSON_DIR = '../data/json/'

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    files = os.listdir(JSON_DIR)
    files.sort()
    files.reverse()
    files = files[:5]
    decrees = []
    for f in files:
        j = json.load(open(JSON_DIR + f))
        decrees.append(j)
    return render_template('home.html', decrees=decrees)


if __name__ == '__main__':
    app.run(debug=True)

