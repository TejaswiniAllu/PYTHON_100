print("Enter string")
s=input()
vowels=['a','e','i','o','u','A','E','I','O','U']
cnt=0
for i in s:
    if i in vowels:
        cnt+=1
print("Number of vowels: ", cnt)
