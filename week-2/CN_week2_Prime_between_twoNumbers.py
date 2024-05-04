#find the primes between two numbers where the numbers are excluding
x,y=[int(i) for i in input("enter two numbers : ").split(",")]
x=x+1
while x<y:
    if x==1 :
        pass
    x=x+1
    d=2
    while d<x:
        _notPrime=x%d==0
        if _notPrime:
            break
        d=d+1
    else:
        print(x,end=",")    
    
     
     
