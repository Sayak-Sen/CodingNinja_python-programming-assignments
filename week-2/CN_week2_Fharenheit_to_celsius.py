"""
Given three values-Start Fahrenheit Value(s),end Fahrenheit value(E) and step Size (W),
you need to convert all Fahrenheit valuesfrom start to end at the gap of W, into their corresponding Celsius
values and print the table

"""

F_start=eval(input("Fahrenheit start value : "))
F_end=eval(input("Fahrenheit end value : "))
stp=eval(input("step size : "))

while F_start<=F_end:
    F=F_start
    C_celsius=int(5*(F-32)/9)
    print(F_start,C_celsius,sep="\t")
    F_start+=stp
    
