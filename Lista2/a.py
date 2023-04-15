#  questao.py
#  Copyright 2022
#  Autor: Henrique Dalmagro

#############################
# Fonte code in Python 3.10 #
#############################


# Main function
def main():
    # Variables
    n1 = int()
    n2 = int()

    # Data input
    n1 = int(input("Digite o 1 numero: "))
    n2 = int(input("Digite o 2 numero: "))

    # Data output
    if n1 > n2:
        print(n1, "E maior que", n2)
    else:
        print(n1, "E menor que", n2)

    return 0


if __name__ == "__main__":
    main()
