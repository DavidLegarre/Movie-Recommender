import re
import time
###
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent
###


def movie_web_scrapper(url):
    id = 0
    title = ""
    rating = 0
    genres = []
    chrome_options = Options()
    ua = UserAgent()
    userAgent = ua.chrome
    chrome_options.add_argument(f'user-agent={userAgent}')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, features='html.parser')

    id_ = "(?<=\/title\/)[^\/]+"

    with open("content.html", "w", encoding='utf-8') as f:
        f.write(content)

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
        "div", attrs={"data-testid": "hero-rating-bar__aggregate-rating__score"}).text
    rating = float(rating_[:-3])
    # Drop last input to genres "back to top"
    # genres.pop()

    driver.quit()

    return id, title, rating, genres


if __name__ == '__main__':
    output = movie_web_scrapper("https://www.imdb.com/title/tt13833688")
    print(output)

    output2 = movie_web_scrapper("https://www.imdb.com/title/tt0068646")
    print(output2)
