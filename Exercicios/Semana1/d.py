# Leitura do salário fixo, total de vendas e percentual de comissão
salario_fixo = float(input("Digite o salário fixo do vendedor: "))
total_vendas = float(input("Digite o total de vendas efetuadas: "))
percentual_comissao = float(input("Digite o percentual de comissão: "))

# Cálculo da comissão e salário final
comissao = (total_vendas * percentual_comissao) / 100
salario_final = salario_fixo + comissao

# Impressão da comissão e salário final na tela
print(f"Comissão do vendedor: R$ {comissao:.2f}")
print(f"Salário final do vendedor: R$ {salario_final:.2f}")
