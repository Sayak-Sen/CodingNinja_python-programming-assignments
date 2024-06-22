#All the prime numbers from 2 to n
n=eval(input("enter a number : "))
def _isPrime(n):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        return True
    return False

def primeNumbersFrom_2_To_n(n):
    for i in range(2,n+1):
        x=_isPrime(i)
        if x:
            print(i)
primeNumbersFrom_2_To_n(n)
