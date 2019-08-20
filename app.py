from flask import Flask
from flask import jsonify
from registerAPI import registerAPI_blueprint
from dataAPI import dataAPI_Blueprint

app = Flask(__name__)
app.register_blueprint(registerAPI_blueprint)
app.register_blueprint(dataAPI_Blueprint)

if __name__ == '__main__':
    app.run()