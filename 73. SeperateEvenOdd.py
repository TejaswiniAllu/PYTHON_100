print("Enter List:")
a = list(map(int, input().split()))
even=[]
odd=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even List: ", even)
print("Odd list: ",  odd)
