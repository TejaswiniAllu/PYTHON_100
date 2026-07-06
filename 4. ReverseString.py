print("Enter a string: ")
s=input()
n=len(s)
rev=""
for i in range(n):
    rev+=s[n-i-1]
print("Reverse of String: ", rev)
