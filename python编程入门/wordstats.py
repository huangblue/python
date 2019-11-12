# wordstats.py
import os
os.chdir('D:\Program Files\python\exercise\data')
keep={'a','b','c','d','e','f','g',
      'h','i','j','k','l','m','n',
      'o','p','q','r','s','t','u'
      'v','w','x','y','z',' ','-',"'"}

def normalize(s):
    """Convert s to a normalized string.
    """
    result = ''
    for c in s.lower():
        if c in keep:
            result += c
    return result


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
            # print(w+'  '+str(d[w]))
        else:
            d[w] =1    
    return d

def print_file_stats(fname):
    """Print statistics for the given file.
    """
    s = open(fname, 'r').read()
    num_chars = len(s)	#在规范化s之前计算字符数
    num_lines = s.count('\n')	#在规范化s之前计算行数
    d = make_freq_dict(s)
    num_words = sum(d[w] for w in d) #计算s包含多少个单词
    
    #创建一个列表，其中的元素由出现次数和单词组成的元组
    #并按出现次数从高到低排列
    lst = [(d[w], w) for w in d]
    lst.sort()   
    lst.reverse()   
    #在屏幕上打印结果
    print("The file '%s' has: " % fname)
    print("	%s	characters" % num_chars)
    print("	%s	lines" % num_lines)
    print("	%s	words" % num_words)
    print("\nThe top 10 most frequent words are:")
    i = 1	# i为列表元素编号
    for count, word in lst[:10]:
        print('%2s. %4s %s' % (i, count, word))
        i += 1

def main():
    print_file_stats('pg8813.txt')

if __name__=='__main__':
   main()
    
