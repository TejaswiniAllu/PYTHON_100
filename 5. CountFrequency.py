print("Enter Array List: ")
a=list(map(int,input().split()))
dict={}
for i in a:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
