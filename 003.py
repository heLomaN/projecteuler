from math import sqrt
num=600851475143
prim=[]
ind=3

while num%2==0:
    num=num/2
sqrtn=sqrt(num)
while (ind<sqrtn) and (num!=1):
    if num%ind==0:
        num/=ind
        prim.append(ind)
        ind-=1
    ind+=1
prim.sort()
print(num,prim[-1])
