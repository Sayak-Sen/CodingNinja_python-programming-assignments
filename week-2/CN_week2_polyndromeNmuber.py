#polyndrome number checker

n=int(input("enter a number : "))
#inverse
invNum=0
temp=n
while temp!=0:
    _mod=temp%10
    invNum=invNum*10+_mod
    temp//=10
#polyndrome check
if n==invNum:
    print(True)
else:
    print(False)
    
    
      
