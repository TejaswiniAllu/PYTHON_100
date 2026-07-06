print("Enter Array List: ")
a=list(map(int,input().split()))
largest=a[0]
for i in range(len(a)):
    if a[i]>largest:
        largest=a[i]
second_largest=a[0]
for i in range(len(a)):
    if a[i]>second_largest and a[i]!=largest:
        second_largest=a[i]
print("Second Largest Number:", second_largest)
