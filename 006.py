from math import pow
num=list(range(1,101))
sumdif=pow(sum(num),2)-sum([x*x for x in num])
print(sumdif)
