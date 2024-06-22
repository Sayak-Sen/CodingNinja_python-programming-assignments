#check the number is prime or not by using function

def _isPrime(n):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        return True
    return False
  
n=int(input("enter a number : " ))
result=_isPrime(n)
print(result)
    
