print("Enter list: ")
a=list(map(int,input().split()))
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j+1]<a[j]:
            a[j+1],a[j]=a[j],a[j+1]
print(a)
