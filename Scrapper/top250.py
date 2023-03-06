from imdb_scrapper import *
import sys
######
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
######
sys.path.append(".")


URL = "https://www.imdb.com/chart/top/"

titles = []
titles_id = []
catalogue = pd.DataFrame(columns=["Title", "Rating", "Genres"])


def add_movie(catalogue, id, title, rating, genres):
    new_movie = {
        "Title": [title],
        "Rating": [rating],
        "Genres": [genres]
    }
    print(new_movie.items())
    new_movie = pd.DataFrame(new_movie, index=[id])
    catalogue = pd.concat([catalogue, new_movie], ignore_index=True)
    return catalogue


if __name__ == '__main__':
    driver, url_list = top_chart_scrapper(URL)

    movies_seen = 0

    for url in url_list:
        data = movie_web_scrapper(driver, url)
        catalogue = add_movie(catalogue, *data)
        movies_seen += 1
        print(f"Movies saved to the database: {movies_seen}")
        if movies_seen == 10:
            break

    driver.quit()

    print(catalogue)

    catalogue.to_csv("Top_250_films.csv")
