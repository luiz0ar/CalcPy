import os

def limpar_tela():
        os.system('cls')

def selecionar_idioma():
    while True:
        print("\nCALCULATOR")
        print("Escolha o idioma / Choose the language:")
        print("1. Português")
        print("2. English")
        escolha = input("\n")

        if escolha == '1':
            idioma = 'pt'
            limpar_tela()
            return idioma
        elif escolha == '2':
            idioma = 'en'
            limpar_tela()
            return idioma
        else:
            print("Opção inválida! Tente novamente. / Invalid option! Try again.")

def traduzir(idioma):
    if idioma == 'pt':
        return {
            "menu": "\nEscolha uma operação:",
            "somar": "1. Somar",
            "subtrair": "2. Subtrair",
            "multiplicar": "3. Multiplicar",
            "dividir": "4. Dividir",
            "sair": "0. Sair",
            "opcao": "Escolha uma opção:",
            "primeiroNum": "Digite o primeiro número:",
            "segundoNum": "Digite o segundo número:",
            "resultado": "O resultado é:",
            "saida": "Adeus...",
            "opcaoInvalida": "Opção inválida! Por favor, escolha uma operação válida."
        }
    else:
        return {
            "menu": "\nChoose a mathematical operation:",
            "somar": "1. Addition",
            "subtrair": "2. Subtract",
            "multiplicar": "3. Multiplication",
            "dividir": "4. Division",
            "sair": "0. Exit",
            "opcao": "Choose an option:",
            "primeiroNum": "Type the first number:",
            "segundoNum": "Type the second number:",
            "resultado": "The result is:",
            "saida": "Bye...",
            "opcaoInvalida": "Please choose a valid operation."
        }

def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Division not possible."
    return x / y

def calcular(idioma):
    mensagens = traduzir(idioma)
    
    while True:
        print(mensagens["menu"])
        print(mensagens["somar"])
        print(mensagens["subtrair"])
        print(mensagens["multiplicar"])
        print(mensagens["dividir"])
        print(mensagens["sair"])

        escolha = input(mensagens["opcao"])

        if escolha == '0':
            print(mensagens["saida"])
            break

        num1 = float(input(mensagens["primeiroNum"]))
        num2 = float(input(mensagens["segundoNum"]))
        
        if escolha == '1':
            print(f"{mensagens['resultado']} {somar(num1, num2)}")
        elif escolha == '2':
            print(f"{mensagens['resultado']} {subtrair(num1, num2)}")
        elif escolha == '3':
            print(f"{mensagens['resultado']} {multiplicar(num1, num2)}")
        elif escolha == '4':
            print(f"{mensagens['resultado']} {dividir(num1, num2)}")
        else:
            print(mensagens["opcaoInvalida"])

if __name__ == "__main__":
    idioma = selecionar_idioma()
    calcular(idioma)
