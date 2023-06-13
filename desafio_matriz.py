"""
*********EXERCÍCIOS COM MATRIZES*******
********************************************
Selecione a opção desejada:
********************************************
1 Preencher uma matriz com números inteiros
2 Imprimir a matriz de números inteiros
3 Imprimir a soma dos elementos de cada linha da matriz
4 Imprimir a soma dos elementos de cada coluna damatriz
5 Imprimir a somados elementos da diagonal principal
6 Imprimir a matriz transposta
7 Imprimir quantidade de elementos pares e impares
8 Imprimir a soma de todos os elementos da matriz
9 Imprimir o maior elemento da matriz e onde se encontra
0 Encerrar o Sistema
********************************************
********************************************
"""
count  = 0
matriz = [[0,0,0], 
          [0,0,0], 
          [0,0,0]]

# Imprimindo cabeçalho
print("***********EXERCÍCIOS COM MATRIZES**********")
print("********************************************")
print("Selecione a opção desejada:")
print("********************************************")

# Fica no sistema enquanto o usuario desejar continuar
while True:
    # Zerando qualquer soma por precaução
    soma = 0

    print("\n********************************************")
    print("1 - Preencher uma matriz com números inteiros")
    print("2 - Imprimir a matriz de números inteiros")
    print("3 - Imprimir a soma dos elementos de cada linha da matriz")
    print("4 - Imprimir a soma dos elementos de cada coluna da matriz")
    print("5 - Imprimir a soma dos elementos da diagonal principal")
    print("6 - Imprimir a matriz transposta")
    print("7 - Imprimir quantidade de elementos pares e ímpares")
    print("8 - Imprimir a soma de todos os elementos da matriz")
    print("9 - Imprimir o maior elemento da matriz e onde se encontra")
    print("0 - Encerrar o Sistema")
    print("********************************************\n")

    try:
        # Recebendo uma opção
        opcao = int(input("\nDigite a opção: "))

    except ValueError: # Erro de conversão
        print("Erro! digite novamente")

        # Chama o menu novamente
        continue

    # Verifica se esta no primeiro loop, e se a opção não é preencher a matriz
    if count == 0 and opcao != 1:
        print("Primeiro e necessario preencher a matriz!\n")
        
        # Preenchendo cada elemento da matriz
        for linha in range(3):
            for coluna in range(3):
                # Entrada de dados
                matriz[linha][coluna] = int(input("Digite o numero: "))
        # Somando 1 ao contador
        count += 1

        # Retorna ao começo do loop
        continue
    
    # Verifica qual opção do programa executar
    match opcao:
        # Prencher matriz
        case 1:
            for linha in range(3):
                for coluna in range(3):
                    # Inserindo o valor na posição da matriz
                    matriz[linha][coluna] = int(input("Digite o numero: "))

        # Imprimir matriz
        case 2:
            for linha in range(3):
                for coluna in range(3):
                    # Imprimindo cada linha
                    print(f"{matriz[linha][coluna]:3}", end=" ")
                # Adicionando quebra de linha
                print()

        # Soma das linhas
        case 3:
            for linha in range(3):
                soma = 0

                # Soma para cada linha
                for coluna in range(3):
                    soma += matriz[linha][coluna]
                
                # Imprimindo a soma
                print(f"Soma da {linha+1}º Linha: {soma}")

        # Soma das colunas
        case 4:
            for coluna in range(3):
                soma = 0

                # Soma cada coluna
                for linha in range(3):
                    soma += matriz[linha][coluna]

                print(f"{soma}")

        # Soma diagonal principal
        case 5:
            soma = 0

            for i in range(3):
                soma += matriz[i][i]

            print(f"{soma}")

        # Matriz transposta
        case 6:
            # Iniciando matriz transposta
            transposta = []

            for l in range(3):
                # Criando uma nova linha
                linha = []

                for c in range(3):
                    linha.append(matriz[c][l])

                transposta.append(linha)

            # Imprimindo matriz
            for linha in transposta:
                print(linha, end="\n")

        # Soma quantidade impar e par
        case 7:
            par = 0
            impar = 0

            for linha in range(3):
                for c in range(3):
                    if matriz[linha][c] % 2 == 0:
                        par += 1
                    else:
                        impar += 1

            print("Quantidade de numeros par:", par)
            print("Quantidade de numeros impar:", impar)

        # Imprimir a soma de todos os elementos da matriz
        case 8:
            soma = 0

            for linha in range(3):
                for coluna in range(3):
                    soma += matriz[linha][coluna]

            print("Soma dos elementos:", soma)

        # Imprimir o maior elemento da matriz e onde se encontra
        case 9:
            maior = 0

            for linha in range(3):
                for coluna in range(3):
                    elemento = matriz[linha][coluna]

                    if elemento > maior:
                        maior = elemento
                        linha = linha
                        coluna = coluna
                        
            print("Maior elemento:", elemento)
            print("Linha:", linha)
            print("Coluna:", coluna)

        case 0:
            print("********************************************")
            print("Encerrando sistema")
            print("********************************************")

            # Encerra o loop
            break
        
        # Qualquer outro valor
        case _:
            print("Opção invalida!")

            # Retorna ao inicio do loop
            continue
    
    # Somando + 1 no contador
    count += 1