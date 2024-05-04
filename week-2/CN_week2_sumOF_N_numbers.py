#Ginen an integer n, find and print the sum of numbers from 1 to n
n=int(input("enter number : "))
x=1
sum=0
while x<=n:
    sum=sum+x
    x=x+1
print("sum of %i numbers is %d"%(n,sum))    
