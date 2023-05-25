"""
Exercício 1) Faça um algoritmo onde o usuário irá alimentar 3 listas com as seguintes 
informações de 10 chuveiros: código, tensão e corrente .O algoritmo deverá :

x - a) Calcular em uma nova lista a potência de cada chuveiro. Considere potência 
tensão x corrente. 
b) Imprimir os códigos dos chuveiros com seus respectivas potências .
x - c) Calcular e imprimir a média das potências.
x - d) Calcular e imprimir quantos chuveiros possuem tensões maiores que 50.
e) Verificar e imprimir o código e a potência do chuveiro mais econômico.
f) Verificar e imprimir o código e a potência do chuveiro menos econômico.
"""

#  questao.py
#  Copyright 2022
#  Autor: Henrique Dalmagro

#############################
# Codigo fonte em Python 3.10 #
#############################


# Main function
def main():
    # Variaveis
    chuveiros = []
    potencias = []

    # Entrada de dados
    print("--- Registrar Chuveiros ---")
    for i in range(1, 11):
        codigo = int(input("Codigo:"))
        tensao = float(input("Tensão: "))
        corrente = float(input("Corrente: "))
        print()
    
        # Processamento 1
        chuveiros.append([codigo, tensao, corrente])


    # Processamento 2
    potencias = [t * c for t, c in zip(chuveiros[1], chuveiros[2])]
    media_potencia = sum(potencias) / len(potencias)
    maior_que_50 = len([t for t in chuveiros[1] if t > 50])
    maior_potencia = potencias.index(max(potencias))
    menor_potencia = potencias.index(min(potencias))

     # Saida de dados
    for i, chuveiro in enumerate(chuveiros):
        print(f"Codigo: {chuveiro[0]}")
        print(f"Potencia: {potencias[i]}")

    print(f"Media das potencias: {media_potencia}")
    print(f"Quantidade de potencias maior que 50: {maior_que_50}")
   
    print("Chuveiro mais econômico\n--------------")
    print(f"Codigo: {chuveiros[0][maior_potencia]}")
    print(f"Potencia: {potencias[maior_potencia]}")

    print("Chuveiro menos econômico\n--------------")
    print(f"Codigo: {chuveiros[0][menor_potencia]}")
    print(f"Potencia: {potencias[menor_potencia]}")

    return 0


if __name__ == "__main__":
    main()
