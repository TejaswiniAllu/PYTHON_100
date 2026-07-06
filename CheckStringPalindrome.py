print("Enter a String: ")
s=input()
n=len(s)
l=0
r=n-1
while l<=r:
    if s[l]!=s[r]:
        print("Not a Palindrome")
        exit()
    l+=1
    r-=1
print("Palindrome")
