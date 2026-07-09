from collections import Counter
print("Enter List: ")
a=list(map(int,input().split()))
a.sort()
freq=Counter(a)
max_freq=max(freq.values())
print("Mode: ",end=" ")
for key,value in freq.items():
    if value==max_freq:
        print(key,end=" ")
