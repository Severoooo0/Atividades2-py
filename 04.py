cand1 = cand2 = cand3 = cand4 = 0
nulos = brancos = 0
total = 0

while True:
    voto = int(input("Digite o voto (0 encerra): "))

    if voto == 0:
        break

    total += 1

    if voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 += 1
    elif voto == 3:
        cand3 += 1
    elif voto == 4:
        cand4 += 1
    elif voto == 5:
        nulos += 1
    elif voto == 6:
        brancos += 1

print("\nResultado da Eleição")
print("Candidato 1:", cand1)
print("Candidato 2:", cand2)
print("Candidato 3:", cand3)
print("Candidato 4:", cand4)
print("Votos nulos:", nulos)
print("Votos em branco:", brancos)

if total > 0:
    print("Percentual de nulos: %.2f%%" % (nulos * 100 / total))
    print("Percentual de brancos: %.2f%%" % (brancos * 100 / total))
