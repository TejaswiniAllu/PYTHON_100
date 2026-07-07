print("Enter string")
s=input()
for i in s:
    if s.count(i)==1:
        print(i)
        exit()
print("No non repeating string")
