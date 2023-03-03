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


if __name__=='__main__':
    print("Hello World")
    movie = Movie("Patata", "450903",2)
    print(movie)