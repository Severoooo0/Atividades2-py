linhas = int(input("Número de linhas: "))
colunas = int(input("Número de colunas: "))

matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input()))
    matriz.append(linha)

nova_matriz = []

for i in range(linhas - 1, -1, -1):
    nova_matriz.append(matriz[i])

print("\nNova matriz:")
for linha in nova_matriz:
    print(linha)
