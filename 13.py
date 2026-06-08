linhas = int(input("Número de linhas: "))
colunas = int(input("Número de colunas: "))

matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input(f"Elemento [{i}][{j}]: ")))
    matriz.append(linha)

elemento = int(input("Digite o elemento a procurar: "))

contador = 0

for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] == elemento:
            contador += 1

print(f"O elemento {elemento} aparece {contador} vez(es) na matriz.")
