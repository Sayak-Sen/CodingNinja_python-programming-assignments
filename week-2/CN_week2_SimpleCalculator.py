"""
Write a program that performs the tasks of a simple calculator. The program should first take an integer as input
and then based on that integer perform the task as given below.

1. If the input is 1, then 2 integers are taken from the user and their sum is printed.
2. If the input is 2, then 2 integers are taken from the user and their difference(1st number - 2nd number) is printed.
3. If the input is 3, then 2 integers are taken from the user and their product is printed.
4. If the input is 4, then 2 integers are taken from the user and the quotient obtained (on dividing 1st number by 2nd number) is printed.
5. If the input is 5, then 2 integers are taken from the user and their remainder(1st number mod 2nd number) is printed.
6. If the input is 6, then the program exits.
7. For any other input, then print "Invalid Operation".
"""
while True:
    n=int(input("enter the correct option : "))
    if n==1:
        x=int(input("enter the first num : "))
        y=int(input("enter the second num : "))
        print("sum of two num is {}".format(x+y))
    elif n==2:
        x=int(input("enter the first num : "))
        y=int(input("enter the second num : "))
        print("difference between two numbers is {}".format(x-y))    
    elif n==3:
        x=int(input("enter the first num : "))
        y=int(input("enter the second num : "))
        print("product of two num is {}".format(x*y))
    elif n==4:
        x=int(input("enter the first num : "))
        y=int(input("enter the second num : "))
        print("quotient is {}".format(x//y))
    elif n==5:
        x=int(input("enter the first num : "))
        y=int(input("enter the second num : "))
        print("remainder is {}".format(x%y))
    elif n==6:
        exit()
    else:
        print("invalid operation")

