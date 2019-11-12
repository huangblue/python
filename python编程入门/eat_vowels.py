# eatvowels.py
def eat_vowels(s):
    #return ''.join([c for c in s if c.lower() not in 'aeiou'])    
    return ''.join(c for c in s if c.lower() not in 'aeiou')
