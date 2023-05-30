# Leitura dos dados de eleitores, votos brancos, nulos e válidos
total_eleitores = int(input("Digite o número total de eleitores: "))
votos_brancos = int(input("Digite o número de votos brancos: "))
votos_nulos = int(input("Digite o número de votos nulos: "))
votos_validos = int(input("Digite o número de votos válidos: "))

# Cálculo dos percentuais
percentual_brancos = (votos_brancos / total_eleitores) * 100
percentual_nulos = (votos_nulos / total_eleitores) * 100
percentual_validos = (votos_validos / total_eleitores) * 100

# Impressão dos percentuais na tela
print(f"Percentual de votos brancos: {percentual_brancos:.2f}%")
print(f"Percentual de votos nulos: {percentual_nulos:.2f}%")
print(f"Percentual de votos válidos: {percentual_validos:.2f}%")
