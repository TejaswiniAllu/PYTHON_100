print("Enter Array List: ")
a=list(map(int,input().split()))
largest=a[0]
for i in range(len(a)):
    if a[i]>largest:
        largest=a[i]
print("Largest Number:", largest)
