from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    #TODO: fetch data from DB
    #TODO: render template with data 
    return 'Toma decretazo!'

if __name__ == '__main__':
    app.run(debug=True)


