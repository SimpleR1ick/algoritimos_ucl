# Leitura do valor pago pelo produto e do preço do produto
valor_pago = float(input("Digite o valor pago pelo produto: "))
preco_produto = float(input("Digite o preço do produto: "))

# Cálculo do troco
troco = valor_pago - preco_produto

# Impressão do troco na tela
print(f"Troco a ser dado: R$ {troco:.2f}")