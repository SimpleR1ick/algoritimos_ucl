#  questao.py
#  Copyright 2022
#  Autor: Henrique Dalmagro

#############################
# Fonte code in Python 3.10 #
#############################

tabela = {
    "norte": [800, 1200],
    "nordeste": [700, 1750],
    "sul": [500, 1380],
    "sudeste": [1000, 2050],
    "centro-oeste": [550, 820],
}   

# Main function
def main():
    global tabela

    # Variables
    nome = str()
    idade = int()
    regiao = str()
    tipo = str()

    # Data input
    while True:
        try:
            nome = input("Digite o nome do passageiro: ")
            idade = int(input("Digite a idade da pessoa: "))
            regiao = input("Digite a região de moradia: ")
            tipo = input("Digite o tipo de passagem Vip(V) ou Comum(C): ")

        except ValueError:
            print("Erro! Digite novamente")

        else:
            tipo = tipo.upper()

            # Valida a idade
            if idade < 0:
                print("Erro! idade invalida\n")
                continue

            # Verifica se a regiao existe
            if not regiao in tabela:
                print("Erro! regiao invalida\n")
                continue
            
            # Verifica o tipo de passagem
            if not tipo in ("V", "C"):
                print("Erro! tipo de passagem invalida")
                continue

            break

    # Process
    total = tabela[regiao][0] if tipo == "V" else tabela[regiao][1]

    # Data output
    print(f"O passegeiro {nome}")

    # Idoso
    if idade > 65:
        print(f"50% de desconto de deve pagar {total * 0.5}")
    # Bebe
    elif idade < 1:
        print("Esta incento de pegamento")
    # Criança
    elif idade <= 5:
        print(f"10% de desconto R${total * 0.9}")
    # Normal
    else:
        print(f"Total a pagar R${total}")

    return 0


if __name__ == "__main__":
    main()
