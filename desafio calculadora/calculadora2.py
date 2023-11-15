def calculadora(opcao, primeiro_num, segundo_num):
  resultado = None

  # Realiza a operação
  if opcao == "1":
    resultado = primeiro_num + segundo_num
  elif opcao == "2":
    resultado = primeiro_num - segundo_num
  elif opcao == "3":
    resultado = primeiro_num * segundo_num
  elif opcao == "4":
    resultado = primeiro_num / segundo_num

  print(f"Resultado: {resultado}")


if __name__ == "__main__":
  opcoes = ["1", "2", "3", "4", "0"]


  while True:
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")

    opcao = input("Digite a opção desejada: ")

    # Validação
    if opcao not in opcoes:
      print("Essa opção é inexistente, coloque uma opção válida.")
      continue

    primeiro_num = float(input("Digite o primeiro valor: "))
    segundo_num = float(input("Digite o segundo valor: "))

    calculadora(opcao, primeiro_num, segundo_num)

# Retorna com o menu
    print()
