#fromstod.py
import os
os.chdir('D:\Program Files\python\exercise\data')
keep={'a','b','c','d','e','f','g',
      'h','i','j','k','l','m','n',
      'o','p','q','r','s','t','u'
      'v','w','x','y','z',' ','-',"'"}
def writefile(filename):
    f=open(filename,'r')
    s=f.read()
    make_freq_dict(s)
    f.close()
    return

def make_freq_dict(s):
    """Returns a dictionary whose keys
       are the words of s, and whose values are the counts of those words.
    """
    s = normalize(s)
    words = s.split()
    d = {}
    for w in words:
        if w in d:
            d[w] +=1
        else:
            d[w] =1
    f=open('pg8813words.txt','w')
    for k in d:
        f.write(k+'  '+str(d[k])+'\n')
    return d

def normalize(s):
    """Convert s to a normalized string.
    """
    result = ''
    for c in s.lower():
        if c in keep:
            result += c
    return result
