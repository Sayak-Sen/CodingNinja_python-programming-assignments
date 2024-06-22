#polindrome number check

n=int(input("enter a number : "))

def polyndromeChecker(n):
    num=n
    sum=0
    while num!=0:
        digit=num%10
        sum=sum*10+digit
        num//=10
    if sum==n:
        print("%i is a polindrome number"%n)
    else:
        print("%i is not a polindrome number"%n)
polyndromeChecker(n)         
        
