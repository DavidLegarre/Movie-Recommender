from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd

URL = "https://www.imdb.com/chart/top/"

driver = webdriver.Chrome("usr/lib/chromium-browser/chromedriver")
titles = []
titles_id = []


if __name__=='__main__':
