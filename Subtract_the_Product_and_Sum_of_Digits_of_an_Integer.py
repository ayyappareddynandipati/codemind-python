n=int(input())
sum=0
mul=1
while (n>0):
    d=n%10
    sum=sum+d
    mul=mul*d
    n=n//10
print(mul-sum)