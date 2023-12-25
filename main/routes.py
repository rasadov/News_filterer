from main import app
from flask import render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import NumberRange
from main.web_news_scraping import get_news


class SearchForm(FlaskForm):
    minimum = IntegerField("Minimum points", default=0)
    maximum = IntegerField("Maximum points", default=100000)
    submit = SubmitField("Submit")

@app.route('/')
@app.route('/home')
def main_page():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        minimum = form.minimum.data
        maximum = form.maximum.data
        print(minimum, "------------")
        return render_template('search.html', form=form, minimum=minimum, maximum=maximum)
    return render_template('search.html', form=form, minimum=0, maximum=0)


@app.route('/hacker-news', methods=["POST", "GET"])
def hacker_news_page():
    form = SearchForm()
    if form.validate_on_submit():
        minimum = form.minimum.data
        maximum = form.maximum.data
        print(minimum, maximum)
        items = get_news(minimum, maximum)
        return render_template("search.html", items=items)
    return render_template('hacker-news.html', form=form)

