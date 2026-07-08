print("Enter list")
a=list(map(int,input().split()))
n=len(a)+1
es=(n*(n+1))//2
asum=sum(a)
print("Missing number: ",es-asum)
