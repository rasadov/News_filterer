import requests
from bs4 import BeautifulSoup

# criteria = int(input("Enter the minimum amount of votes: "))

URl = 'https://news.ycombinator.com/?p='
# website we are going to grab data from


def points(span):
    points = span.text.split()[0]
    return int(points)
    # returns amount of points from score class


def get_link(tr):
    return tr.select('a')[1].get('href')
    # returns a link in athing class


def filter_points(span, min_points, max_points):
    points_of_span = points(span)
    if points_of_span > min_points and points_of_span < max_points:
        return True
    # returns True if amount of points more than minimum


# filtered by the amount of points
def get_news(min_points, max_points):
    articles = []
    for i in range(1, 5):
        res = requests.get(URl + str(i))
        soup = BeautifulSoup(res.text, 'html.parser')
        # getting access to website

        links = soup.select('.athing')
        votes = soup.select('.score')

        # grabbing data which will be needed for filtration

        ids = {}
        for i in votes:
            if filter_points(i, min_points, max_points):
                ids[(i.get('id')[6:])] = points(i)
            # selecting articles with points more than 150

        articles += ([[f'{i.text}', f'{ids[i.get("id")]} votes', get_link(i)] for i in links if i.get('id') in ids])
    return articles