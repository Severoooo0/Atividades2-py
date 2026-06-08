n = int(input())

soma = 0
m = 1

for i in range(1, n + 1):
    soma += i / m
    m += 2

print(f"{soma:.2f}")
