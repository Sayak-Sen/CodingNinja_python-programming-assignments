#check the number is prime or not
n=int(input("enter the number : "))
d=2
while d<n:
    is_prime=n%d==0
    if is_prime:
        print("given number %i is not prime"%n)
        break
    d+=1
else:
    print("given number {} is  prime".format(n))
