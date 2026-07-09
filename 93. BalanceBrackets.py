print("Enter Expression:")
s = input()
stack = []
pairs = {')': '(', '}': '{', ']': '['}
balanced = True
for ch in s:
    if ch in "({[":
        stack.append(ch)
    elif ch in ")}]":
        if not stack or stack[-1] != pairs[ch]:
            balanced = False
            break
        stack.pop()
if balanced and not stack:
    print("Balanced")
else:
    print("Not Balanced")
