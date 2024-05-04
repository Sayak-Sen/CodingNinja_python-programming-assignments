#print multiple of 3 from m upto n
m=int(input("enter start value : "))
n=int(input("enter end value : "))
for i in range(m,n+1):
    if i%3==0:
        print(i)
            
