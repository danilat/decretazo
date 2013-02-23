from flask import Flask
from flask import render_template, url_for

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    #TODO: fetch data from DB
    #TODO: render template with data 
    #return url_for('static', filename='style.css')
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)


