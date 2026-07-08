from collections import Counter
print("Enter string:")
s=input()
freq=Counter(s)
for key,value in freq.items():
    if value>1:
        print(key,end=" ")
        
