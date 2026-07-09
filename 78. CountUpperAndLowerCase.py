print("Enter string: ")
s=input()
lower=0
upper=0
for i in s:
    if i.isupper():
        upper+=1
    if i.islower():
        lower+=1
print("Upper: ",upper)
print("Lower: ",lower)
