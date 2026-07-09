from collections import Counter
print("Enter Number:")
n = input()
freq = Counter(n)
for digit, count in freq.items():
    print(digit, ":", count)
