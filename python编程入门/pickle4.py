#pickle4
import pickle
import os
os.chdir('D:\Program Files\python\exercise\data')
test = r'test.txt'
def sayhi(name):
    print("hello",name)
    print("hello2",name)
with open(test,'rb') as f:
    data = pickle.loads(f.read())
print('data>>',data)
print(data['func']('hdf'))
