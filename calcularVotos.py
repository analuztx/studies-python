vBranco = float(input("Digite o valor de votos em branco: "))
vNulos = float(input("Digite o valor de votos nulos: "))
vValidos = float(input("Digite o valor de votos válidos: "))

totalEleitores = vBranco + vNulos + vValidos

pBranco = (vBranco * 100) / totalEleitores
pNulos = (vNulos * 100) / totalEleitores
pValidos = (vValidos * 100) / totalEleitores

print(f"Percentual de voto em branco: {pBranco} \nPercentual de voto nulo: {pNulos} \nPercentual de voto válido: {pValidos}")