print("Enter list1: ")
a=list(map(int,input().split()))
print("Enter list2: ")
b=list(map(int,input().split()))
res=[]
for i in a:
    if i in b:
        res.append(i)
print("Common Elements", res)
