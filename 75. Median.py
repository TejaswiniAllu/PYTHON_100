print("Enter List:")
a = list(map(int, input().split()))
a.sort()
n = len(a)
if n % 2 == 0:
    median = (a[n//2 - 1] + a[n//2]) / 2
else:
    median = a[n//2]
print("Median =", median)
