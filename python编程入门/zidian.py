def zidian():
    d ={'a': 2,'long': 1,'time': 1,'ago':1,'in':1,'galaxy':1,'far': 2, 'away': 1}
    lst=[]
    for k in d:
        pair=(d[k],k)
        lst.append(pair)
    lst.sort()
    lst.reverse()
    for count, word in lst:
        print('%4s %s' % (count, word))
    #return lst

