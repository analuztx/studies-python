from math import pi

raio = float(input("Digite o valor do raio: "))
altura = float(input("Digite o valor da altura: "))

volume = pi * pow(raio,2) * altura

print(f"O volume do cilindro é: {volume}")