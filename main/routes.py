from main import app
from flask import render_template, redirect, url_for, request , jsonify
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

@app.route('/hacker-news', methods=["POST", "GET"])
def hacker_news_page():
    form = SearchForm()
    if request.method == "GET":
        return render_template('hacker-news.html', form=form)
    if request.method == "POST":
        if form.validate_on_submit():
            minimum = form.minimum.data
            maximum = form.maximum.data
            page = request.args.get('page', 1, type=int)
            # items = get_news(minimum, maximum)
            return redirect(url_for('search', minimum=minimum, maximum=maximum, page=page))
        else:
            if not form.minimum.data:
                minimum = 0
            else:
                minimum = form.minimum.data
            if not form.maximum.data:
                maximum = 100000
            else:
                maximum = form.maximum.data
            page = request.args.get('page', 1, type=int)
            # items = get_news(minimum, maximum)
            return redirect(url_for('search', minimum=minimum, maximum=maximum, page=page))


@app.route('/search', methods=["GET"])
def search():
    minimum = request.args.get('minimum', type=int)
    maximum = request.args.get('maximum', type=int)
    page = request.args.get('page', 1, type=int)
    items = get_news(minimum, maximum)
    
    # Pagination logic
    start_index = (page - 1) * 5
    end_index = start_index + 5
    paginated_items = items[start_index:end_index]

    # Calculate the total number of pages
    total_pages = len(items) // 5 + (len(items) % 5 > 0)

    return render_template("search.html",minimum=minimum, maximum=maximum, items=paginated_items, page=page, total_pages=total_pages)

