total=0
s=input('Enter a number (or "done"): ')
while True:    
    s=input('Enter a number (or "done"): ')
    if s!='done':
        total=total+int(s)
    else:
        break
        
print('The sum is '+str(total))
