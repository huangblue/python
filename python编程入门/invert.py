#invert.py
def invert(x):
    try:
        return 1 / x
    except ZeroDivisionError:
        return 'error1'
    finally:
        print('invert(%s) done' % x)
