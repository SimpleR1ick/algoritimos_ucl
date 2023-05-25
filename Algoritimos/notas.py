# Notas do alunos
notas = [4.0, 5.7, 8.8, 9.0, 7.2, 2.3, 4.3, 8.9, 6.6, 1.2]

# Declaração de variaveis
aprovados = []
maior_nota = 0
menor_nota = max(notas)
soma = 0

# Percorrendo as notas
for nota in notas:
    # Verifica se esta aprovado
    if nota >= 7:
        aprovados.append(nota)  

        # Registra a maior nota
        if nota > maior_nota:
            maior_nota = nota

    else:
        # Registra a menor nota
        if nota < menor_nota:
            menor_nota = nota
    
    # Registra as notas entre 5 e 10
    if 5 <= nota <= 10:
        soma += nota

# Saida de dados
print("Quantidade de alunos aprovados: ", aprovados.len())
print("Media das notas do alunos aprovados: ", max(aprovados) / len(aprovados))
print("Maior nota registrada: ", maior_nota)
print("Menor nota registrada: ", menor_nota)