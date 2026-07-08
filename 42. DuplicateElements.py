from collections import Counter
print("Enter list")
a=list(map(int,input().split()))
freq=Counter(a)
for key,value in freq.items():
    if value>1:
        print(key,end=" ")
        
