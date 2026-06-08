gabarito = []

print("Digite o gabarito:")
for i in range(10):
    gabarito.append(input(f"Questão {i+1}: ").upper())

maior = 0
menor = 10
total = 0
soma = 0

while True:
    acertos = 0

    for i in range(10):
        resp = input(f"Resposta da questão {i+1}: ").upper()

        if resp == gabarito[i]:
            acertos += 1

    print("Nota:", acertos)

    total += 1
    soma += acertos
    maior = max(maior, acertos)
    menor = min(menor, acertos)

    if input("Outro aluno? (S/N): ").upper() != "S":
        break

print("\nMaior acerto:", maior)
print("Menor acerto:", menor)
print("Total de alunos:", total)
print("Média da turma:", round(soma / total, 2))
