print("Enter dictionary:")
a=eval(input())
print("Sorted dictionary: ", sorted(a.items(), key=lambda x:x[1]))
