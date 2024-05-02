#You are given first three entries of an arithmetic progression. You have to calculate the common difference and print it.

firstEntry=int(input("first entry : "))
secondEntry=int(input("second entry : "))
thirdEntry=int(input("third entry : "))
cd1=secondEntry-firstEntry
cd2=thirdEntry-secondEntry
if cd1==cd2:
    cd=cd1=cd2
    print("common difference is %d "%cd)
else:
    print("the given numbers are not in arithmatic progression")
