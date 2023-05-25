#  questao.py
#  Copyright 2022
#  Autor: Henrique Dalmagro

#############################
# Fonte code in Python 3.10 #
#############################


# Main function
def main():
    """
    Main function
    """
    # Variables
    salario = 0
    desconto = 0

    # Data input
    nome = input("Digite o nome: ").capitalize()
    cargo = int(input("Digite a carga horaria semanal: "))
    vale = input("Possui vale transporte? S/N: ").upper()
    titulo = int(input("1 - Graduaçao\n2 - Especialista\n3 - Mestre\n4 - Doutor"))
    tempo = int(input("Digite o tempo de serviço: "))

    # Process
    # Verifica a titulação do professor
    if titulo == 1:
        valor = 47.0
    elif titulo == 2:
        valor = 57.0
    elif titulo == 3:
        valor = 70.0
    else:
        valor = 105.0

    # Verifica se possui vale transporte
    if vale in ('S', 'SIM'):
        desconto = valor * 0.06

    # Descontando o valor do vale transporte
    valor -= desconto

    # Verifica se possui um binomio de tempo
    if tempo >= 24:
        for _ in range(0, tempo // 24):
            valor += 0.05

    # Calcula o salario final
    salario = valor * cargo * tempo

    # Data output
    print(f"O {nome} recebera no total R$ {salario}")

    return 0


if __name__ == "__main__":
    main()
