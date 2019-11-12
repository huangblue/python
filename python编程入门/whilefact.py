n=int(input('Enter an integer>=0: '))
fact=1
i=2
while i<n+1:
    fact=fact*i
    i=i+1
print(str(n)+'factorial is ' + str(fact))
