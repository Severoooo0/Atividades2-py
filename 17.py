linhas = int(input("Número de linhas: "))
colunas = int(input("Número de colunas: "))

matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input()))
    matriz.append(linha)

quadrada = True

if linhas != colunas:
    quadrada = False

for linha in matriz:
    if len(linha) != colunas:
        quadrada = False

print(quadrada)
