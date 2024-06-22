#find the value of nCr

n,r=[int(x)for x in input("enter n,r : ").split(",")]

nfact=1
for i in range(1,n+1):
    nfact=nfact*i

rfact=1
for j in range(1,r+1):
    rfact=rfact*j
    
n_r_fact=1
for k in range(1,n-r+1):
    n_r_fact=n_r_fact*k

nCr=nfact//(rfact*n_r_fact)    


print("{}C{} is equal to {}".format(n,r,int(nCr)))    
