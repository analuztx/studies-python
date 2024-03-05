atualSalario = float(input("Digite o valor do salário atual: "))
valorPercentual = float(input("Digite o valor do percentual: "))

novoSalario = atualSalario + (atualSalario * valorPercentual) / 100

print(f"O novo salário é: {novoSalario}")