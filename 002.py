#python 2.7.3
from math import log,ceil
num=4000000
#fibo(n)~=0.44*1.618^n
minn=ceil(log(num*3,1.618))
print(minn)
sumfibo=0
fibo=[0,1,2]
for x in xrange(3,int(minn)):
    if fibo[2]>num:
        print(fibo[2],x)
        break
    sumfibo+=fibo[2]
    fibo[0]=fibo[1]+fibo[2]
    fibo[1]=fibo[0]+fibo[2]
    fibo[2]=fibo[0]+fibo[1]

print(sumfibo)

