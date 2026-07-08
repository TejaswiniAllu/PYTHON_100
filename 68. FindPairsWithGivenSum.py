print("Enter List:")
a = list(map(int, input().split()))
print("Enter Target Sum:")
target = int(input())
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == target:
            print(a[i], a[j])
