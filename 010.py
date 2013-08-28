num=2000000


numlist=[2,3,5]
for ind in range(1,num/6):
    numlist+=[6*ind+1,6*ind+5]
numlist+=[num-1,num]

numlen=len(numlist)
ind=0
tmp=0
while ind < numlen:
    indi=ind+1
    if numlist[ind]>tmp:
        print(numlist[ind])
        tmp+=1000
    while indi <numlen:
        if numlist[indi]%numlist[ind]==0:
            del numlist[indi]
            indi-=1
            numlen-=1
        indi+=1
    ind+=1

print(sum(numlist))
