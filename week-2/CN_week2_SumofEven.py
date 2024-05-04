#sum of even numbers
n=int(input("enter a number : "))
x=0
even=0
while x<=n:
    _isEven=x%2==0
    if _isEven:
        even=even+x
    x+=1    
print(f"sum of even numbers are {even}")        
        
