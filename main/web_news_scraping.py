import requests
from bs4 import BeautifulSoup

# criteria = int(input("Enter the minimum amount of votes: "))

URl = 'https://news.ycombinator.com/?p='
# website we are going to grab data from

def filter_points(span, min_points, max_points):
    points_of_span = int(span.text.split()[0])
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
                ids[(i.get('id')[6:])] = int(i.text.split()[0]) # ids[id] = amount of points
            # selecting articles with points more than 150

        articles += ([[f'{i.text}', f'{ids[i.get("id")]} votes', i.select('a')[1].get('href')] for i in links if i.get('id') in ids])
    return articles

if __name__ == '__main__':
    news = get_news(100,400)
    # for i in news:
        # print(i)