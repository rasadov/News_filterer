from main import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import NumberRange

class NewsForm(FlaskForm):
    min_points = IntegerField(validators=[NumberRange(min=0)])
    max_points = IntegerField(validators=[NumberRange(min=min_points)])
    submit = SubmitField(label='Search')

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/hacker-news')
def hacker_news_page():
    # form = NewsForm()
    items = ["hello"]
    return render_template('hacker-news.html', items=items)

