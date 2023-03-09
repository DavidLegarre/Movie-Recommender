import pandas as pd
import numpy as np


def init_user(user_sample: pd.DataFrame()):
    n = len(user_sample)
    r_ratings = np.random.rand(n,1).round(2)*5
    user_sample["User_ratings"] = r_ratings

        
