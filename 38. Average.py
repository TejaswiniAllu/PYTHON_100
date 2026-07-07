print("Enter array list: ")
a=list(map(int,input().split()))
sum=0
for i in a:
    sum+=i
print("Average", sum//len(a))
