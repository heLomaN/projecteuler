b=1.0

while b<501:
    a=1000*(500-b)/(1000-b)
    if a%1==0:
        c=1000-a-b
        if a*a+b*b==c*c:
            print(a*b*c)
    b+=1
