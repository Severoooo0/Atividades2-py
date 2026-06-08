atleta = input("Nome do atleta: ")

notas = []

for i in range(7):
    nota = float(input("Nota: "))
    notas.append(nota)

print("\nAtleta:", atleta)
for nota in notas:
    print("Nota:", nota)

melhor = max(notas)
pior = min(notas)
media = (sum(notas) - melhor - pior) / 5

print("\nResultado final:")
print("Atleta:", atleta)
print("Melhor nota:", melhor)
print("Pior nota:", pior)
print(f"Média: {media:.2f}")
