#  questao.py
#  Copyright 2022
#  Autor: Henrique Dalmagro

#############################
# Fonte code in Python 3.10 #
#############################


# Main function
def main():
    # Variables
    nome = str()
    salario = float()

    # Data input
    while True:
        try:
            nome = input("Digite o nome do jogador: ")
            salario = float("Digite o salario: ")

        except ValueError:
            print("Erro! Dados invalidos")

        else:
            if nome.isnumeric():
                print("Erro! Nome invalido :/")
                continue

            break
    
    # Process
    if salario <= 5000:
        salario *= 0.2

    elif salario <= 15000:
        salario *= 0.1

    # Data output
    print("Salario reajustado: ", salario)

    return 0


if __name__ == "__main__":
    main()
