print("Enter number: ")
n=int(input())
length=len(str(n))
temp=n
sum=0
while temp!=0:
    d=temp%10
    sum+=d**length
    temp//=10
if sum==n:
    print(n,"is an armstrong number")
else:
    print(n, "is not an armstrong number")
