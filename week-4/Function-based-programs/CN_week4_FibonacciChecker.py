# Create a function that determines whether a given number N belongs to the Fibonacci sequence.
# If N is found in the Fibonacci sequence, the function should return true; otherwise, it should return false.
n=int(input("enter a number : "))

def Fibonacci_Generator(n):
    a=0
    b=1
    if n<0:
        print("sorry invalid input ")
    elif n==0:
        print("true")
    elif n==1:
        print("true")
    else:
        term=1
        while term<=n:
            c=a+b
            a=b
            b=c
            if c==n:
                print("true")
                break
            term+=1
        else:
            print("false")
Fibonacci_Generator(n)
