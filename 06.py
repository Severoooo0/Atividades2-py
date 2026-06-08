while True:
    nome = input("Nome do atleta: ")

    if nome == "":
        break

    saltos = []

    for i in range(5):
        salto = float(input(f"{i+1}º salto: "))
        saltos.append(salto)

    melhor = max(saltos)
    pior = min(saltos)

    media = (sum(saltos) - melhor - pior) / 3

    print("\nAtleta:", nome)
    print()

    ordem = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]

    for i in range(5):
        print(f"{ordem[i]} Salto: {saltos[i]} m")

    print()
    print(f"Melhor salto: {melhor} m")
    print(f"Pior salto: {pior} m")
    print(f"Média dos demais saltos: {media:.1f} m")

    print("\nResultado final:")
    print(f"{nome}: {media:.1f} m\n")
