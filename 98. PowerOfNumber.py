print("Enter Base:")
base = int(input())
print("Enter Exponent:")
exp = int(input())
result = 1
for i in range(exp):
    result *= base
print("Power =", result)
