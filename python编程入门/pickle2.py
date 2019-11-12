#pickle2.py
import pickle
import os
os.chdir('D:\Program Files\python\exercise\data')
#dump：
li = [11,22,33]
pickle.dump(li,open('db','wb'))
 
#load
ret = pickle.load(open('db','rb'))
print(ret)
