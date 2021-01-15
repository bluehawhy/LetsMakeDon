import os, sys, pathlib

#refer to path from 
sys.path.append(str(pathlib.Path(__file__).parent.absolute()).split('/_app')[0])


main_path =  str(pathlib.Path(__file__).parent.absolute()).split('/_app')[0]
db_fullname = os.path.join(main_path,'_db')
print(db_fullname)
