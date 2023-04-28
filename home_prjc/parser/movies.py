from pprint import pprint

import requests
from bs4 import BeautifulSoup

URL = "https://megogo.net/ru/films"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 "
                  "Safari/537.36"
}


def get_html(url):
    response = requests.get(url, headers=HEADERS)
    return response


def get_data(html, size=None):
    soup = BeautifulSoup(html, 'html.parser')
    size = int(size) if size else None
    movies = soup.find_all("div", class_="card videoItem orientation-portrait size-normal", limit=size)
    movies_list = []
    for movie in movies:
        info = movie.find('div', class_="card-content video-content")
        every_movie = {
            "title": movie.find('div', class_="card-content video-content").find('a').string,
            "url": movie.find('div', class_="card-content video-content").find('a').get("href"),
            "image": movie.find("img").get("src")
        }
        movies_list.append(every_movie)
    # pprint(movies_list)
    return movies_list


def parser(size=None):
    html = get_html(URL)
    if html.status_code == 200:
        movie = get_data(html.text, size)
        return movie
    raise Exception("Error in parser!")

# data = parser(2)
# pprint(data)
