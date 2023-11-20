# Uma nova loja de cosméticos abriu no seu bairro e pediram para você elaborar um sistema que imprime na tela na frente da loja os novos produtos que chegaram. 
# O sistema da loja já tem um array com os produtos, você precisa apenas imprimir eles no terminal, um por um.

# Obs: Como desafio opcional, tente imprimir cada produto com a frase "Temos [produto] à venda!" (ex. "Temos máscaras faciais à venda!"). 

# lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']

# Desafio obrigatório
for produto in lista_produtos:
    print(produto)

# Desafio opcional utilizando o comando "format"
for produto in lista_produtos:
    print("Temos {} à venda!".format(produto))
