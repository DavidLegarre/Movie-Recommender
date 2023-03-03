import re
###
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
###


def movie_web_scrapper(url):
    id = 0
    title = ""
    rating = 0
    genres = []
    driver = webdriver.Chrome()

    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, features='html.parser')

    id_ = "(?<=\/title\/)[^\/]+"


    # Obtain Id
    match = re.search(id_, url)
    id = match.group()

    # Obtain Title
    title = soup.find('span', class_='sc-afe43def-1 fDTGTb').text

    # Find all ratings   
    genres_span = soup.find_all('span', class_='ipc-chip__text')
    for genre in genres_span:
        genres.append(genre.text)
    
    # Obtain rating
    rating = float(soup.find('span', class_='sc-e457ee34-1 squoh').text)

    # Drop last input to genres "back to top"
    genres.pop()

    return id, title, rating, genres


if __name__ == '__main__':
    output = movie_web_scrapper("https://www.imdb.com/title/tt13833688")
    print(output)
