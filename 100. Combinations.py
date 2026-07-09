from itertools import combinations
print("Enter String:")
s = input()
print("Combinations:")
for i in range(1, len(s) + 1):
    for comb in combinations(s, i):
        print("".join(comb))
