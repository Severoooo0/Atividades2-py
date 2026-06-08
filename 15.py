l = int(input())
c = int(input())

matriz = []

for i in range(l):
    linha = []
    for j in range(c):
        linha.append(int(input()))
    matriz.append(linha)

maior = matriz[0][0]
menor = matriz[0][0]

for linha in matriz:
    for num in linha:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print("Maior:", maior)
print("Menor:", menor)
