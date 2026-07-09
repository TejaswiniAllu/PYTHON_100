print("Enter string: ")
s=input()
words=s.split()
lar=words[0]
for word in words:
    if len(word)>len(lar):
        lar=word
print("Largest Word: ",lar)
