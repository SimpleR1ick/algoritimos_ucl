# Leitura do peso do prato montado em gramas
peso_prato_gramas = float(input("Digite o peso do prato montado (em gramas): "))

# Cálculo do valor a pagar em reais
preco_quilo = 12.00
peso_prato_quilo = peso_prato_gramas / 1000  # convertendo de gramas para quilos
valor_pagar = preco_quilo * peso_prato_quilo

# Impressão do valor a pagar na tela
print(f"Valor a pagar: R${valor_pagar:.2f}")
