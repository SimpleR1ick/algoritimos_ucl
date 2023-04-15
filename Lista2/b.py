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
    
    # Data output
    if numero > 0:
        print("Maior que zero")
    elif numero == 0:
        print("Igual a zero")
    else:
        print("Menor que zero")

    return 0


if __name__ == "__main__":
    main()
