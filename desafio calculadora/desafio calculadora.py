class Calculadora:
    def __init__(self, numero1, numero2, op):
        self.numero1 = numero1
        self.numero2 = numero2
        self.op = op

    def calcula(self):
        if self.op == 1:
            return self.numero1 + self.numero2
        elif self.op == 2:
            return self.numero1 - self.numero2
        elif self.op == 3:
            return self.numero1 * self.numero2
        elif self.op == 4:
            return self.numero1 / self.numero2
        else:
            print("Opção inválida, escolha uma opção de operação válida.")
            return None
# Achei melhor fazer o usuário colocar uma opção válido do que imprimir zero, como o exercício pediu
def main():
    while True:
        print("\nEscolha uma operação: 1. Soma - 2. Subtração - 3. Multiplicação - 4. Divisão - 5. Sair")
        operador = input
        operador = int(input("Digite o número da operação desejada: "))
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
# Pode ser feito um tratamento de erros com uma mensagem para o usuário, se caso coloque caracteres ou não digite nada
        if operador == 5:
            break

        calc = Calculadora(numero1, numero2, operador)
        result = calc.calcula()

        if result is not None:
            print("O resultado da operação é:", result)


if __name__ == "__main__":
    main()
