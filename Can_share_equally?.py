x,y=map(int,input().split())
z=(x*1)+(y*2)
if z%2==0 :
    if x==0 and y%2!=0 :
        print("NO")
    else :
        print("YES")
else:
    print("NO")