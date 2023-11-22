#Problema

#Um dono de uma loja entra em contato com você com a seguinte situação:

#Estamos modernizando nossa loja e precisamos de um novo sistema de controle de estoque. 
#  Geralmente anotamos todos os produtos que temos disponíveis, e quando um dos produtos acaba,
# substituimos ele por algum outro produto. 
#  Ouvi dizer que vocês podem fazer um sistema para a gente que mostra a lista com todos nossos 
# produtos, e nos deixa alterar um produto por outro.
#  Além disso, estamos pensando em ampliar nosso armazém, 
# para ter mais espaço para mais produtos.
# Então, se puderem fazer com que o sistema nos permita adicionar mais produtos à lista,
#e qualquer outra coisa que acharem necessário, seria muito bom.
# Desde já agradeço!

produtos = []

produtos = []

# Lista de produtos
def listar_produtos():
  for i in range(len(produtos)):
    print(produtos[i])

# Alteração de um produto
def alterar_produto(produto_atual, produto_novo):
  for i in range(len(produtos)):
    if produtos[i] == produto_atual:
      produtos[i] = produto_novo

# Adiciona um produto à lista
def adicionar_produto(produto):
  produtos.append(produto)

# Loop de repetição principal
while True:
# Lista os produtos
  listar_produtos()

# Interação com o usuário para realizar a ação desejada
  print("O que você deseja fazer?")
  print("1 - Listar produtos")
  print("2 - Alterar produto")
  print("3 - Adicionar produto")
  opcao = input("Opção: ")

# Realiza a ação desejada
  if opcao == "1":
    listar_produtos()
  elif opcao == "2":
    produto_atual = input("Digite o produto atual: ")
    produto_novo = input("Digite o produto novo: ")
    alterar_produto(produto_atual, produto_novo)
  elif opcao == "3":
    produto = input("Digite o novo produto: ")
    adicionar_produto(produto)
  else:
    print("Opção inválida.")
