# aula de array 
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

#Solução


#Listas: para armazenar os produtos da loja.
#For: para adicionar a lista de produtos.
#Adicionar mais dados na lista: para adicionar novos produtos à lista.
#Adicionar mais produtos na lista: para adicionar novos produtos à lista.
#Remover mais produtos na lista: para remover produtos da lista.
#Mostrar todos os produtos da lista: para mostrar todos os produtos da lista.

# Funções
def criar_lista():
  return []

def adicionar_produto(lista, produto):
  lista.append(produto)

def remover_produto(lista, produto):
  lista.remove(produto)

def listar_produtos(lista):
  for produto in lista:
    print(produto)

# Função principal
def main():
  # Cria uma lista vazia
  lista_produtos = criar_lista()

  # Interação com o usuário
  while True:
    # Opções disponíveis
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Listar produtos")
    print("4. Sair")

    # Escolha do usuário
    escolha = input("Escolha uma opção: ")

    # Opção 1: Adicionar produto
    if escolha == "1":
      produto = input("Digite o produto: ")
      adicionar_produto(lista_produtos, produto)

    # Opção 2: Remover produto
    elif escolha == "2":
      produto = input("Digite o produto a ser removido: ")
      remover_produto(lista_produtos, produto)

    # Opção 3: Listar produtos
    elif escolha == "3":
      listar_produtos(lista_produtos)

    # Opção 4: Sair
    elif escolha == "4":
      break

    # Opção inválida
    else:
      print("Opção inválida.")

if __name__ == "__main__":
  main()
