#temperature conversion list

start=int(input("enter the starting value of temperature : "))
end=int(input("enter the ending value of temperature : "))
step=int(input("enter the step size of temperature : "))

def temperature_conversion(start,end,step):
    print("\n F \t C")
    while start<=end:
        c=(start-32)*(5/9)
        print(start,end="\t")
        print(int(c))
        start+=step
temperature_conversion(start,end,step)
    
