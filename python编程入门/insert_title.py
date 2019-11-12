#insert_title.py
import os
os.chdir('D:\Program Files\python\exercise\data')
def insert_title(title, fname = 'story.txt'):
    f = open(fname, 'r+')
    temp = f.read()
    temp = title + '\n\n' + temp
    f.seek(0) #让文件指针指向文件开头
    f.write(temp)
