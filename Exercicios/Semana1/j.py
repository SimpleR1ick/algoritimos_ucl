# Leitura do nome da pessoa e do ano de nascimento
nome = input("Digite o nome da pessoa: ")
ano_nascimento = int(input("Digite o ano de nascimento da pessoa: "))

# Cálculo da idade
ano_atual = 2023 # Utilizamos o ano atual como exemplo
idade = ano_atual - ano_nascimento

# Impressão do nome e idade da pessoa na tela
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
