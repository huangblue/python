#picle1.py
import pickle
#dumps
li = [11,22,33]
r = pickle.dumps(li)
print(type(r))
print(r)
 
#loads
result = pickle.loads(r)
print(result)
