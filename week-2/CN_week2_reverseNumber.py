"""
Reverse an Integer

Write a program to generate the reverse of a given number N. Print the corresponding reverse number.

Note : If a number has trailing zeros, then its reverse will not include them.
For e.g., reverse of 10400 will be 401 instead of 00401.

"""
num=int(input("enter a number : "))
reversed_num = 0
while num != 0:

    digit = num % 10

    reversed_num = reversed_num * 10 + digit

    num //= 10
print(reversed_num)


