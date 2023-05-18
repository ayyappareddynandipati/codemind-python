num=int(input())
a,b=0,1
while(True):
    c=a+b
    if (c>num):
        h1=b
        h2=c
        break
    a=b
    b=c
x1=abs(h1-num)
x2=abs(h2-num)
if(x1==x2):
    print(h1,h2)
elif (x1<x2):
    print(h1)
else:
    print(h2)