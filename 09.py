n = int(input("Digite a quantidade de termos: "))

soma = 0
den = 1

for num in range(1, n + 1):
    termo = num / den
    soma += termo

    print(f"{num}/{den}", end="")

    if num < n:
        print(" + ", end="")

    den += 2

print(f"\n\nSoma = {soma:.2f}")
