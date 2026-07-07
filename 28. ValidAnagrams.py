from collections import Counter
print("Enter two strings:")
a=input()
b=input()
if sorted(a)==sorted(b) and Counter(a)==Counter(b):
    print("Anagrams")
else:
    print("Not Anagrams")
