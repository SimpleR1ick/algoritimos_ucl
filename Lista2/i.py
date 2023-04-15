"""A concessionária de veículos “CARANGO VELHO” está vendendo os seus veículos 
com desconto. Faça um algoritmo que calcule e exiba o valor do desconto e o valor 
a ser pago pelo cliente. O desconto deverá ser calculado de acordo com o ano do 
veículo. Até 2000 - 12% e acima de 2000 - 7%
"""

def main():
    # Declerando variaveis
    desconto = float()
    preco_veiculo = float()
    ano_veiculo = int()

    while True:
        try:
            preco_veiculo = float(input("Digite o valor do veiculo: "))
            ano_veiculo = int(input("Digite o ano de fabricação: "))

            break

        except ValueError:
            print("Valores incorretos")

    # Processamento
    if ano_veiculo <= 2000:
        desconto = preco_veiculo * 0.12
    else:
        desconto = preco_veiculo * 0.07

    preco_veiculo -= desconto

    print("Desconto final: ", desconto)


if __name__ == '__main__':
    main()