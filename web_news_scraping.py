import requests
from bs4 import BeautifulSoup

criteria = int(input("Enter the minimum amount of votes: "))

URl = 'https://news.ycombinator.com/?p='
# website we are going to grab data from


def points(span):
    points = span.text.split()[0]
    return int(points)
    # returns amount of points from score class


def get_link(tr):
    return tr.select('a')[1].get('href')
    # returns a link in athing class


def filter_points(span, min_points):
    if points(span) > min_points:
        return True
    # returns True if amount of points more than minimum


# filtered by the amount of points
for i in range(1, 4):
    res = requests.get(URl + str(i))
    soup = BeautifulSoup(res.text, 'html.parser')
    # getting access to website

    links = soup.select('.athing')
    votes = soup.select('.score')

    # grabbing data which will be needed for filtration

    ids = {}
    for i in votes:
        if filter_points(i, criteria):
            ids[(i.get('id')[6:])] = points(i)
        # selecting articles with points more than 150

    for i in links:
        if i.get('id') in ids:
            print(f'{i.text} --- has {ids[i.get("id")]} votes: ', get_link(i))
        # prints article of selected previously ids


# if __name__ == '__main__':
#     pdb.run('exit')
