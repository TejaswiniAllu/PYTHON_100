print("Enter List:")
a = list(map(int, input().split()))
prod=1
for i in a:
    prod*=i
print("Product= ",prod)
