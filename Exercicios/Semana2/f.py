# Ler os três valores inteiros distintos
valor1 = int(input("Digite o primeiro valor inteiro: "))
valor2 = int(input("Digite o segundo valor inteiro: "))
valor3 = int(input("Digite o terceiro valor inteiro: "))

# Colocar os valores em ordem crescente
if valor1 < valor2 and valor1 < valor3:
    primeiro = valor1

    if valor2 < valor3:
        segundo = valor2
        terceiro = valor3
    else:
        segundo = valor3
        terceiro = valor2

elif valor2 < valor1 and valor2 < valor3:
    primeiro = valor2

    if valor1 < valor3:
        segundo = valor1
        terceiro = valor3
    else:
        segundo = valor3
        terceiro = valor1
else:
    primeiro = valor3
    
    if valor1 < valor2:
        segundo = valor1
        terceiro = valor2
    else:
        segundo = valor2
        terceiro = valor1

# Escrever os valores em ordem crescente
print(primeiro, segundo, terceiro)
