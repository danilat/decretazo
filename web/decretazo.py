import os
import json
import re
from flask import Flask
from flask import render_template, url_for

JSON_DIR = 'data/'

app = Flask(__name__, static_url_path='')

def read_files():
    files = os.listdir(JSON_DIR)
    files.sort()
    return files

def get_year(filename):
    match = re.findall('BOE-A-\w+', filename)[0]
    year = match.split('BOE-A-')[1]
    if not years.count(year) > 0:
        years.append(year)
    return year

years = []
files = read_files()

@app.route('/')
def index():
    decrees = []
    for f in files:
        j = json.load(open(JSON_DIR + f))
        year = get_year(f)
        decrees.append(j)
    return render_template('home.html', decrees=decrees, years=years)

@app.route('/<selected_year>')
def show(selected_year):
    decrees = []
    for f in files:
        year = get_year(f)
        if selected_year == year:
            j = json.load(open(JSON_DIR + f))
            decrees.append(j)
    print years
    return render_template('show.html', decrees=decrees, year=selected_year, years=years)

if __name__ == '__main__':
    app.run(debug=True)

