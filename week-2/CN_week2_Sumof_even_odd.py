"""
Write a program to input an integer 'n' and
print the sum of all its even digits and the sum of all its odd digits separately.
"""
n=int(input("enter a number : "))
digit=0
sum_OF_even=0
sum_OF_odd=0
while n!=0:
    x=n%10
    even_checker=x%2==0
    if even_checker:
        sum_OF_even=sum_OF_even+x
    else:
        sum_OF_odd=sum_OF_odd+x
    n //=10    
print("sum of all even digits is %i"%sum_OF_even)
print("sum of all odd digits is %i"%sum_OF_odd)
