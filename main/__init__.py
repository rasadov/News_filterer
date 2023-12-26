from flask import Flask
from flask_redis import FlaskRedis
import redis

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a637a56ab80d8a3ba645ac50'

from main import routes