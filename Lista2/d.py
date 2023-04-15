#  questao.py
#  Copyright 2022
#  Autor: Henrique Dalmagro

#############################
# Fonte code in Python 3.10 #
#############################


# Main function
def main():
    # Variables
    numero = int()

    # Data input
    numero = int(input("Digite o numero: "))

    # Process
    if numero > 80:
        print("Maior que oitenta")
    elif numero < 25:
        print("Igual a zero")
    elif numero == 40:
        print("Menor que zero")

    return 0


if __name__ == "__main__":
    main()
