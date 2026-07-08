print("Enter List: ")
a=list(map(int,input().split()))
print("Enter key: ")
key=int(input())
a.sort()
check=False
l=0
h=len(a)-1
while l<=h:
    mid=(l+h)//2
    if a[mid]==key:
        check=True
        break
    elif a[mid]<key:
        l=mid+1
    else:
        h=mid-1
if check:
    print("Element Found")
else:
    print("Element Not Found")
