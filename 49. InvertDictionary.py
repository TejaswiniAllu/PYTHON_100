print("Enter dictionary:")
d = eval(input())
inverted = {}
for key, value in d.items():
    inverted[value] = key
print("Inverted Dictionary:", inverted)
