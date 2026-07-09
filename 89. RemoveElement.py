print("Enter List:")
a = list(map(int, input().split()))
print("Enter element to remove:")
x = int(input())
result = []
for i in a:
    if i != x:
        result.append(i)
print("Updated List:", result)
