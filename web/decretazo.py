import os
import json
import re
from flask import Flask
from flask import render_template, url_for

JSON_DIR = '../data/json/'

app = Flask(__name__, static_url_path='')

def read_files():
    files = os.listdir(JSON_DIR)
    files.sort()
    files.reverse()
    return files

@app.route('/')
def index():
    decrees = []
    years = {}
    for f in read_files():
        j = json.load(open(JSON_DIR + f))
        decrees.append(j)
    return render_template('home.html', decrees=decrees)

@app.route('/<year>')
def show(year):
    decrees = []
    for f in read_files():
        match = re.findall('BOE-A-\w+', f)[0]
        file_year = match.split('BOE-A-')[1]
        if year == file_year:
            j = json.load(open(JSON_DIR + f))
            decrees.append(j)
    return render_template('show.html', decrees=decrees, year=year)

if __name__ == '__main__':
    app.run(debug=True)

