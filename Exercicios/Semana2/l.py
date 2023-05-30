#  l.py
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
    diaria = int()
    consumo = float()
    subtotal = float()
    total = float()

    tipos = {
        "A": 150,
        "B": 100,
        "C": 75,
        "D": 50
    }
        
    # Data input
    while True:
        try:
            nome = input("Nome do hospede: ")
            tipo = input("Tipo de apartamento: ")
            diaria = int(input("Quantidade de diarias: "))
            consumo = float(input("Valor em consumo: "))

        except ValueError:
            print("Dados invalidos, digite novamente\n")

        else:
            # Converte para maiusculo
            tipo = tipo.upper()

            # Verifica se o tipo de apartamento existe
            if not tipo in tipos:
                print("Erro! tipo de apto não existe")
                continue

            # Verifica se a diaria e valida
            if diaria <= 0:
                print("Erro! numero de diarias menor que 0")
                continue

            # Verifica se o consumo e valido
            if consumo < 0:
                print("Erro! consumo negativo")
                continue

            # Encerra a expressão
            break    
    
    # Process
    subtotal = tipos[tipo] * diaria
    total = (subtotal + consumo) * 0.10

    # Data output
    print(f"A conta total do hospode {nome} foi:")
    print(f"Apartamento: {tipo}")
    print(f"Numero diarias: {diaria}")
    print(f"Consumo interno: ", {consumo})
    print(f"Subtotal: {subtotal} com 10%")
    print(f"Valor total final: {total}")

    return 0


if __name__ == "__main__":
    main()
