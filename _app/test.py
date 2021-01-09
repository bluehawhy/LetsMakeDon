import pandas as pd


df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]

for i in df:
    print(i)




