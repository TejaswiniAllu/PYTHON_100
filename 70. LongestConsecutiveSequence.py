print("Enter List:")
a = list(map(int, input().split()))
a = sorted(set(a))
longest = 1
current = 1
for i in range(1, len(a)):
    if a[i] == a[i - 1] + 1:
        current += 1
    else:
        longest = max(longest, current)
        current = 1
longest = max(longest, current)
print("Length of Longest Consecutive Sequence:", longest)
