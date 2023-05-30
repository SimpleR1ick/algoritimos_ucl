# Leitura do preço do litro da gasolina e valor disponível para abastecer
preco_litro = float(input("Digite o preço do litro da gasolina: "))
valor_disponivel = float(input("Digite o valor disponível para abastecer: "))

# Cálculo da quantidade de litros de gasolina
litros_gasolina = valor_disponivel / preco_litro

# Impressão da quantidade de litros de gasolina na tela
print(f"Quantidade de litros de gasolina: {litros_gasolina:.2f}")
