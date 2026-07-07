print("Enter string")
s=input()
cnt=0
for i in s:
    if i.isdigit():
        cnt+=1
if cnt==len(s):
    print("Yes")
else:
    print("No")
