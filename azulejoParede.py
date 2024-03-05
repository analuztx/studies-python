alturaPA = float(input("Digite a altura da parede: "))
larguraPA = float(input("Digite a largura da parede: "))

alturaAZ = float(input("Digite a altura do azulejo: "))
larguraAZ = float(input("Digite a largura do azulejo: "))

areaParede = larguraPA * alturaPA
areaAzulejo = larguraAZ * alturaAZ

total = areaParede / areaAzulejo

print(f"O total de azulejos para essa parede seria: {total}")