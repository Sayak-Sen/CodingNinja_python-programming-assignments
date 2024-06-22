#find the value of nCr by using function

n=int(input("enter a value of n: "))
r=int(input("enter another value of r :"))
def fact(n):  #defining a factroial function
    """factorial function"""
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

nfact=fact(n) #call the function and passing the value and store into a variable
rfact=fact(r)
n_r_fact=fact(n-r)
nCr=nfact//(rfact*n_r_fact)

print(f"value of {n}C{r} is {int(nCr)}")

        
