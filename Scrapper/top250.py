import sys
######
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
######
sys.path.append(".")

from Classes.movie import *

URL = "https://www.imdb.com/chart/top/"

driver = webdriver.Chrome()
titles = []
titles_id = []
catalogue = pd.DataFrame()


def add_movie(catalogue, id, title, rating):
    new_movie = {
        "Title": title,
        "Rating": rating,
    }
    new_movie = pd.DataFrame(new_movie, index=[id])
    catalogue = pd.concat([catalogue, new_movie], axis=0)
    return catalogue


if __name__ == '__main__':
    print("Hello World")
    catalogue = add_movie(catalogue, 98403, "Hola", 4)
    print(catalogue)
