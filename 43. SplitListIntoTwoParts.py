print("Enter list:")
a = list(map(int, input().split()))
mid = len(a) // 2
print("First part:", a[:mid])
print("Second part:", a[mid:])
