import pandas as pd
import requests
import bs4 as bs
from sqlalchemy import create_engine


import os, sys, pathlib
#refer to path from 
sys.path.append(str(pathlib.Path(__file__).parent.absolute()).split('/_app')[0])


df = pd.DataFrame([[1, 2], [3, 4]], columns=['a','c'])
print(df)

df = df.append(pd.DataFrame([[6, 5], [4, 4]], columns=['a','c']), ignore_index=True)

print(df)

print('hello world')