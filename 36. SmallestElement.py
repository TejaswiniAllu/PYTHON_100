print("Enter array list: ")
a=list(map(int,input().split()))
smallest=a[0]
for i in a:
    if i<smallest:
        smallest=i
print("Smallest: ",smallest)
