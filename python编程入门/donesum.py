total=0
s=input('Enter a number (or "done"): ')
while s!='done':
    total=total+int(s)
    s=input('Enter a number (or "done"): ')        
print('The sum is '+str(total))
