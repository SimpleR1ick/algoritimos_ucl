

"""
Faça um algoritimo que registre em 4 listas os seguintes:
    dados, codigo, descrição, categoria (percecivel ou não perecivel),preço de custo.

 O algoritimo deve calcular em uma outra lista o preco de venda de cada produto. 
 Considere que produtos da categoria perecivel devem possuir 15% de lucro 
 e produtos não pereciveis 25% de lucro, 
 
 Fazer para 6 produtos com entrada informada pelo usuario

O algoritimo deve retornar:
- A relação dos produtos contendo: codigo, nome, preco de venda
- A media dos preços de vendas do produtos da categoria perecivel e não perecivel
-
"""

produtos = []
pereciveis = 0
n_pereciveis = 0

def criar_produto(codigo, descricao, categoria, preco):
    return {
        "codigo": codigo,
        "descricao": descricao,
        "categoria": categoria,
        "preco": preco,
        "lucro": 0
    }

for _ in range(0, 4):
    codigo = int(input("Codigo: "))
    descricao = input("Descrição: ")
    categoria = int(input("perecivel(1), não perecivel(2): "))
    preco = float(input("Preco: "))

    produto = criar_produto(codigo, descricao, categoria, preco)

    # Calculando preço de venda do produto
    if produto["categoria"] == 1:
        # 15% de lucro
        produto["lucro"] = preco * 1.15
    else: 
        # 25% de lucro
        produto["lucro"] = preco * 1.25

    produtos.append(produto) 

for produto in produtos:
    if produto["cateogira"] == 1:
        pereciveis += produto["lucro"]