from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
jwt = JWTManager(app)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

from routes import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
