#checking nCr by function of two parameters
n=eval(input("enter n : "))
r=eval(input("enter r : "))

#define factorial function
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

#define nCr
def nCr(n,r):
    n_fact=fact(n) #call the fact() function
    r_fact=fact(r)
    n_r_fact=fact(n-r)
    ans=n_fact//(r_fact*n_r_fact)
    return ans

#call the function and store the value into the variable
answer=nCr(n,r)
print(f"{n}C{r} is {answer}")

    
