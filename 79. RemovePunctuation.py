import string
print("Enter String: ")
s=input()
res=""
for i in s:
    if i not in string.punctuation:
        res+=i
print(res)
