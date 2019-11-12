# txtstats.py
import os
os.chdir('D:\Program Files\python\exercise\data')
def file_stats(fname):
    """Print statistics for the given file.
    """
    s = open(fname, 'r').read()
    num_chars = len(s)
    num_lines = s.count('\n')
    num_words = len(normalize(s).split())
    print("The file '%s' has: " % fname)
    print(" %s characters" % num_chars)
    print(" %s lines" % num_lines)
    print(" %s words" % num_words)
    
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
