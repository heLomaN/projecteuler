#python 2.7.3
num=float(1000)

num3=(num-1)//3
num5=(num-1)//5
num15=(num-1)//15
sum3=(num3+1)*num3*3/2
sum5=(num5+1)*num5*5/2
sum15=(num15+1)*num15*15/2
sumall=sum3+sum5-sum15
print(num3,num5,num15,sumall)

