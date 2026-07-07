print("Enter number")
n=int(input())
cnt=0
while n!=0:
    cnt+=1
    n//=10
print("Number of Digits: ",cnt)
