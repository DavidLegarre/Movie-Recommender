import pandas as pd
from utils import init_user

data = pd.read_csv("Top_250_films.csv")

user_sample = data.sample(n=10)

if __name__ == '__main__':
    print("Starting...")
    print(user_sample.head())
    init_user(user_sample)
    print(user_sample.head())
