print("Enter two numbers: ")
a=int(input())
b=int(input())
x=a
y=b
while b!=0:
    a,b=b,a%b
print("LCM: ",(x*y)//a)
