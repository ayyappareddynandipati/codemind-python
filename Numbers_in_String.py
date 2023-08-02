s=input()
lst = []
for i in s:
    if i.isdigit():
        lst.append(int(i))
print(sum(lst))