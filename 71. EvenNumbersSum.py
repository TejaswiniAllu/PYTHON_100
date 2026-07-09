print("Enter List:")
a = list(map(int, input().split()))
sum=0
for i in a:
    if i%2==0:
        sum+=i
print("Sum of even numbers: ",sum)
