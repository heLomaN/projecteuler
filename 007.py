#埃拉托色尼筛选法也许能用

primelist=[2]
primecount=1

isPrime=True
num=3
while primecount<10001:
    isPrime=True
    for ii in primelist:
        if ii*ii>num:
            break
        if num%ii==0:
            isPrime=False
            break;
    if isPrime:
        primelist.append(num)
        primecount+=1
    num+=1

print(len(primelist),primelist[-1])
