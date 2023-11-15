def calcular_idade(ano_nascimento: int):
    return 2022 - ano_nascimento
def main():
    nome = input("Digite seu nome completo: ")

    while True:
        try:
            ano_nascimento = int(input("Digite seu ano de nascimento (1922-2021): "))

            if ano_nascimento < 1922 or ano_nascimento > 2021:
                raise ValueError

            break
        except ValueError:
            print("Ano de nascimento inválido.")

    idade = calcular_idade(ano_nascimento)

    print(f"Olá, {nome}. Você tem {idade} anos (ou completará esse ano).")

if __name__ == "__main__":
    main()
