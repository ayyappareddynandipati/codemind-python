import math
h,m=map(int,input().split(':'))
a=abs((30*h)-(5.5*m))
b=360-a
if a<b:
    print("{:.1f}".format(a))
else :
     print("{:.1f}".format(b))