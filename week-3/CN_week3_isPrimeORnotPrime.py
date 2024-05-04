#using "for loop" check if the given number is prime or not
n=int(input("enter the number : "))
for d in range(2,n):
    isPrime=n%d==0
    if isPrime:
        print("given number %i is not prime "%n)
        break
else:
     print("given number %i is prime "%n)
