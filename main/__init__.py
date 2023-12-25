from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a637a56ab80d8a3ba645ac50'

from main import routes