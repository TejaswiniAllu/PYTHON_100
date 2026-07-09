from itertools import permutations
print("Enter String:")
s = input()
perm = permutations(s)
print("Permutations:")
for p in perm:
    print("".join(p))
