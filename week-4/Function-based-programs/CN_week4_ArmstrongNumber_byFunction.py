# check Armstrong number
"""
An Armstrong number is a number (with 'k' digits) such that the sum of its digits raised to 'kth' power is equal to the number itself.
For example, 371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371.

"""

n=input("enter a number:")
def checkArmstrong(n):
    i=len(n)
    sum=0
    num=int(n)
    while num!=0:
        x=num%10
        sum=sum+pow(x,i)
        num//=10
    if sum==int(n):
        return "true"
    else:
        return "false"
print(checkArmstrong(n))

    
