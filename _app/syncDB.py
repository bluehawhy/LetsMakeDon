import pandas as pd
from sqlalchemy import create_engine

import os, sys, pathlib
#refer to path from 
sys.path.append(str(pathlib.Path(__file__).parent.absolute()).split('_app')[0])




db_path = os.path.join(str(pathlib.Path(__file__).parent.absolute()).split('_app')[0],'_db')


def syncpdtodb():
    url = "http://kind.krx.co.kr/corpgeneral/corpList.do?method=download"
    df = pd.read_html("http://kind.krx.co.kr/corpgeneral/corpList.do?method=download", header=0)[0]
    engine = create_engine("sqlite:///%s/stockList.db" %db_path)
    df.to_sql('stocklist', con=engine, if_exists='replace',index_label='index')
    return 0


def getStockPrice (Stocks):
    engine = create_engine("sqlite:///%s/stockList.db" %db_path)
    df = pd.DataFrame({'name' : ['User 6', 'User 7']})
    df.to_sql('StockPrice', con=engine, if_exists='replace',index_label='index')
    return 0


syncpdtodb()
#getClosingPrice('abc')
