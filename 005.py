num=20
iscounted=[False for x in range(num)]

#ŷ������㷨---���������
def maxgcd(a,b):
    #a>b
    c=a%b
    while(c!=0):
        a=b
        b=c
        c=a%b
    return b

big=num
while num>0:
    big=big*num/maxgcd(big,num)
    num-=1

print(big)
