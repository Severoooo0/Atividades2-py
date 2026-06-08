linhas = int(input("Número de linhas: "))
colunas = int(input("Número de colunas: "))

matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input(f"Elemento [{i}][{j}]: ")))
    matriz.append(linha)

transposta = []

for j in range(colunas):
    linha = []
    for i in range(linhas):
        linha.append(matriz[i][j])
    transposta.append(linha)

print("\nMatriz Transposta:")
for linha in transposta:
    print(linha)
