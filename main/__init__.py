from flask import Flask
from flask_redis import FlaskRedis
import redis

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a637a56ab80d8a3ba645ac50'
app.config['SQLALCHEMY_DATABASE_URI'] = "redis://:password@localhost:5000/news.db"
db = redis.Redis(host='localhost', port=5000, decode_responses=True)



from main import routes