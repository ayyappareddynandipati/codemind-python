s=input()
c=0
lst=list(s)
for i in lst:
    if i.isdigit():
        c+=1
if c==0:
    print("Doesn't contain digit")
else :
    print("Contains",c,"digit")