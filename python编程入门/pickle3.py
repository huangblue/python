#pickle3.py
import os
import pickle
os.chdir('D:\Program Files\python\exercise\data')
test = r'test.txt'
def sayhi(name):
    print("hello",name)

    info = {'':'','age':32,'func':sayhi}

    print(pickle.dumps(info))

    #with open(test,'wb') as f:
    f=open(test,'wb')
    f.write( pickle.dumps(info) )
