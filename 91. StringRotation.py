print("Enter First String:")
s1 = input()
print("Enter Second String:")
s2 = input()
if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Strings are Rotations")
else:
    print("Strings are Not Rotations")
