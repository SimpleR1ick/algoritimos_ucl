#  j.py
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
    while True:
        try: 
            num = int(input("Digite o numero: "))

            break

        except ValueError:
            print("Erro! Digite novamente")
    
    # Data output
    if num in range(100, 201):
        print("Esta contido no intervalo!")
    else:
        print("Não esta contido!")

    return 0


if __name__ == "__main__":
    main()
