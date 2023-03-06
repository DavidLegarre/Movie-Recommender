import re
import time
###
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent
###


def build_webdriver():
    # Configure Chrome_options
    # Add usser-agent so IMDb anti bot options do not trigger
    chrome_options = Options()
    ua = UserAgent()
    userAgent = ua.chrome
    chrome_options.add_argument(f'user-agent={userAgent}')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--allow-running-insecure-content')
    # Headless option so that the browser does not show
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    return driver


def top_chart_scrapper(url):
    driver = build_webdriver()
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")
    title_columns = soup.find_all("td", attrs={
        "class" : "titleColumn"
    })

    movie_list = []

    for title_ in title_columns:
        title_ = title_.find("a", href=True)
        title = title_["href"]
        movie_list.append("https://www.imdb.com"+title)

    return driver, movie_list


def movie_web_scrapper(driver, url):
    id = 0
    title = ""
    rating = 0
    genres = []

    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, features='html.parser')

    id_ = "(?<=\/title\/)[^\/]+"

    # Obtain Id
    match = re.search(id_, url)
    id = match.group()

    # Obtain Title
    # Remove " - IMDb" from the title
    pattern = " - IMDb"
    title = soup.find('title').text
    title = title.replace(pattern, "")
    pattern = "\ \([0-9]*\)"
    title = re.sub(pattern, "", title)

    # Find all genres
    genres_a = soup.find("div", {"data-testid": "genres"})
    genres_a = genres_a.find_all('a')
    for genre in genres_a:
        genres.append(genre.text)

    # Obtain rating
    # rating = float(soup.find('span', class_='sc-e457ee34-1 squoh').text)
    rating_ = soup.find(
        "div",
        attrs={
            "data-testid": "hero-rating-bar__aggregate-rating__score"
        }).text
    rating = float(rating_[:-3])

    return id, title, rating, genres


if __name__ == '__main__':
    url_list = top_chart_scrapper("https://www.imdb.com/chart/top/")
