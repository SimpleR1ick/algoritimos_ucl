#  questao.py
#  Copyright 2022
#  Autor: Henrique Dalmagro

#############################
# Fonte code in Python 3.10 #
#############################


# Main function
def main():
    # Variables
    salario_minino = float()
    salario = float()
    reajuste = float()

    # Data input
    salario_minino = float(input("Digite o valor do salario: "))
    salario = float(input("Digite o salario do funcionario: "))

    # Process
    if salario <= salario_minino * 3:
        reajuste = 0.50

    elif salario <= salario_minino * 10:
        reajuste = 0.20

    elif salario <= salario_minino * 20:
        reajuste = 0.15

    else:
        reajuste = 0.10

    # Data output
    salario += salario * reajuste

    print("Salario final:", salario)

    return 0


if __name__ == "__main__":
    main()
