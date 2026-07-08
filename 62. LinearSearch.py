print("Enter List: ")
a=list(map(int,input().split()))
print("Enter key: ")
key=int(input())
check=False
for i in range(len(a)):
    if a[i]==key:
        check=True
        break
print("Element Found" if check else "Not Found")
