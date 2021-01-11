import pandas as pd
from sqlalchemy import create_engine
import sqlite3


def syncDBandDataframe(dbfile,dataframe):
    conn = sqlite3.connect(dbfile)
    c = conn.cursor()
    #c.execute('''DROP TABLE IF EXISTS person_age;''')
    #c.execute('''
    #          CREATE TABLE person_age
    #          (id INTEGER PRIMARY KEY ASC, age INTEGER NOT NULL)
    #          ''')
    conn.commit()
    conn.close()

    ##### Create original table

    #engine = create_engine("sqlite:///example.db")
    #sql_df = pd.DataFrame({'id' : [1, 2], 'age' : [18, 42]})

    #sql_df.to_sql('person_age', engine, if_exists='append', index=False)


    #### Extra data to insert/update

    #extra_data = pd.DataFrame({'id' : [2, 3], 'age' : [44, 95]})
    #extra_data.set_index('id', inplace=True)

    #### extra_data.to_sql()  with row update or insert option

    #expected_df = pd.DataFrame({'id': [1, 2, 3], 'age': [18, 44, 95]})
    #expected_df.set_index('id', inplace=True)
