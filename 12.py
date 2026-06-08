n = int(input("Digite a ordem da matriz: "))

matriz = []
soma_principal = 0
soma_secundaria = 0

for i in range(n):
    linha = []

    for j in range(n):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(valor)

        if i == j:
            soma_principal += valor

        if i + j == n - 1:
            soma_secundaria += valor

    matriz.append(linha)

print("Soma da diagonal principal:", soma_principal)
print("Soma da diagonal secundária:", soma_secundaria)
