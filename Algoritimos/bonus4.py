# Variaveis
sorteados = []
apostados = []
count = 0

print("------------Mega-Sena-----------")

# Recebeo s numeros sorteados
for i in range(1, 7):
    sorteados.append(int(input(f"Digite o {i}º numero: ")))

print("--------------------------------")
# Recebe os numeros apostados
for i in range(1, 7):
    apostados.append(int(input(f"Digite o {i}º apostado: ")))

# Verifica numeros poastados
for apostado in apostados:
    if apostado == sorteados[i]:
        count += 1


# Verifica se venceu
print("\nA aposta", (count == 6)*"e Vencedora!" or "não ganhou :/")