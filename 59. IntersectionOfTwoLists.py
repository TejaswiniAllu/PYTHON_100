print("Enter two lists: ")
a=list(map(int,input().split()))
b=list(map(int,input().split()))
res=[]
for i in a:
    if i in b:
        res.append(i)
print(res)
