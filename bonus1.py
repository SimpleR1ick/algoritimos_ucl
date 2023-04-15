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
    tipo = str()
    mins = int()

    conta = 0

    # Data input
    while True:
        try:
            nome = input("Digite o nome do cliente: ")
            tipo = input("Digite o tipo de conta (R) ou (C): ")
            mins = int(input("Digite a quantidade de minutos: "))

        except ValueError:
            print("Erro! digite novamente")

        else:
            # Transforma o tipo para maiusculo
            tipo = tipo.upper()

            # Verifica se o tipo de conta e valido
            if not tipo in ("C", "R"):
                print("Erro! tipo de cliente invalido")
                continue
            # Verifica se o tempo não e negativo
            if mins < 0:
                print("Erro! minutos negativos")
                continue
    
            break

    # Process
    if tipo == "C":
        # Verifica se excedeu os minutos
        if mins > 100:
            conta = (mins - 100) * 0.5 + 30
        else:
            conta = mins * 0.3
    else:
        conta = mins * 0.25

    # Verifica o tipo de conta
    tipos = "Residencial" if tipo == "R" else "Comercial"

    # Data output
    print(f"A fatura do cliente {nome}")
    print(f"Conta {tipos}, Total: {conta:.2f}")

    return 0


if __name__ == "__main__":
    main()
