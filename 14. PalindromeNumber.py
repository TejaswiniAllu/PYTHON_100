print("Enter number: ")
n=int(input())
temp=n
rev=0
while temp!=0:
    d=temp%10
    rev=rev*10+d
    temp//=10
if rev==n:
    print(n, "is a palindrome")
else:
    print(n, "is not palindromw")
