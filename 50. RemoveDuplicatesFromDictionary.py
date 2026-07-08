print("Enter dictionary:")
d=eval(input())
result={}
seen=set()
for key, value in d.items():
    if value not in seen:
        result[key]=value
        seen.add(value)
print("Dictionary after removing duplicate values:")
print(result)
