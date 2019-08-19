from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'



@app.route('/data', methods = ['POST'])
def post_data():
    pass


@app.route('/register', methods ='[POST]')
def register_client():
    pass

if __name__ == '__main__':
    app.run()