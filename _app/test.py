import pandas as pd
import requests
import bs4 as bs

url = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download'
df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)
#print(type(df))
#print(df[0])
#for i in df:
#    print(i)

base_url = 'https://finance.naver.com/item/sise_day.nhn?code=005930&page='
res = requests.get(base_url)
print(res.content)
html = bs(res.content,'html.parser')
table0 = html.find('table',{'class':'type2'})


