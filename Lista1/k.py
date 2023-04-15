# Leitura do nome, peso e altura da pessoa
nome = input("Digite o nome da pessoa: ")
peso = float(input("Digite o peso (em kg) da pessoa: "))
altura = float(input("Digite a altura (em metros) da pessoa: "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Impressão do nome e IMC da pessoa na tela
print(f"Nome: {nome}")
print(f"IMC: {imc:.2f}")
