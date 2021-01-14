import os
import pathlib

import pandas as pd

import requests
import bs4 as bs

from sqlalchemy import create_engine


from . import databaseHandler as dh



#df_filename = 'abc.db'
#db_fullname = os.path.join(pathlib.Path(__file__).parent.absolute().parent,'_db',df_filename)


def syncpdtodb():
    url = "http://kind.krx.co.kr/corpgeneral/corpList.do?method=download"
    df = pd.read_html("http://kind.krx.co.kr/corpgeneral/corpList.do?method=download", header=0)[0]
    engine = create_engine("sqlite:..///example.db")
    df.to_sql('test', con=engine, if_exists='append')
    return 0
    

#dh.syncDBandDataframe(db_fullname,'aa','ss')



#print(type(df))
#print(df[0])
#print(df[0])
#print(type(df[0]))
#print(df['종목코드'].values.tolist())
#for i in df:
#    print(i)

# f = i["종목코드"].astype("int64", copy=False)
# print("{:06d}".format(f))


#base_url = "https://finance.naver.com/item/sise_day.nhn?code=005930&page="
#base_url = "https://finance.naver.com/item/sise_day.nhn?code=005560&page="
#base_url = "https://finance.naver.com/item/sise_day.nhn?code=005560&page="
#base_url = "https://finance.naver.com/item/sise_day.nhn?code=114140&page="


# res = requests.get(base_url)
# print(res.content)
# html = bs(res.content,'html.parser')
# table0 = html.find('table',{'class':'type2'})
