print("Enter n:")
n = int(input())
for i in range(1, n + 1):
    print("\nMultiplication Table of", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
