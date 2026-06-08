faixa1 = faixa2 = faixa3 = faixa4 = 0

while True:
    num = float(input("Digite um número: "))

    if num < 0:
        break
    elif num <= 25:
        faixa1 += 1
    elif num <= 50:
        faixa2 += 1
    elif num <= 75:
        faixa3 += 1
    elif num <= 100:
        faixa4 += 1

print("\nResultado:")
print("[0-25]:", faixa1)
print("[26-50]:", faixa2)
print("[51-75]:", faixa3)
print("[76-100]:", faixa4)
