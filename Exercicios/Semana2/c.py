#  questao.py
#  Copyright 2022
#  Autor: Henrique Dalmagro

#############################
# Fonte code in Python 3.10 #
#############################


# Main function
def main():
    # Variables
    num = int()

    # Data input
    print("Descobrindo se um numero e impar ou par\n")
    num = int(input("Digite um numero: "))    

    # Data output
    if num % 2 == 0:
        print("Par")
    else:
        print("Impar")

    return 0


if __name__ == "__main__":
    main()
