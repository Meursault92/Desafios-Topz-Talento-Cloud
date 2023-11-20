# Declare dois arrays, cada um com um mínimo de cinco elementos, e imprima eles no terminal usando o comando print(). 
# O primeiro array deve conter os produtos de uma loja da sua escolha (loja de comida, materiais de construção, música, etc).
# O segundo array deve conter os anos de nascimento de familiares e amigos seus.
# Lembre-se de usar nomes descritivos para nomear cada variável, e de usar o tipo de dado apropriado para cada lista 
# (strings, booleanos, números inteiros, floats).

# Array do tipo string da loja de instrumentos musicais
produtos = ["Guitarra", "Bateria", "Violão", "Microfone", "Caixa de som"]

# Array do tipo inteiro de anos de nascimento de Família e amigos
anos_nascimento = [1990, 1995, 2000, 2005, 2010]

# Impressão dos arrays
print("Produtos da loja de música:")
for produto in produtos:
    print(produto)

print("Anos de nascimento de familiares e amigos:")
for ano_nascimento in anos_nascimento:
    print(ano_nascimento)
# Para realizar o comando "print()", utilizei um loop for. 
# Para cada elemento do array, imprimo o elemento usando a função print().
# No loop do primeiro array, usei o operador in para verificar se o elemento atual da lista é uma string. 
