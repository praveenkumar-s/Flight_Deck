from flask import Flask
from flask import jsonify
from registerAPI import registerAPI_blueprint

app = Flask(__name__)
app.register_blueprint(registerAPI_blueprint)


if __name__ == '__main__':
    app.run()