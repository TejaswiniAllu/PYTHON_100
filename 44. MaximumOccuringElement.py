from collections import Counter
print("Enter list:")
a=list(map(int,input().split()))
freq=Counter(a)
sorted_freq=sorted(freq.items(), key=lambda x:x[1], reverse=True)
print("Maximum Occuring Element: ", sorted_freq[0][0])
