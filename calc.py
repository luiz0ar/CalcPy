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
            "menu": "Escolha uma operação:",
            "somar": "1. Somar",
            "subtrair": "2. Subtrair",
            "multiplicar": "3. Multiplicar",
            "dividir": "4. Dividir",
            "sair": "0. Sair",
            "opcao": "Escolha uma opção:",
            "primeiroNum": "Digite o primeiro número:",
            "segundoNum": "Digite o segundo número:",
            "resultado": "O resultado é:",
            "resultadoAnterior": "Resultado anterior:",
            "saida": "Adeus...",
            "opcaoInvalida": "Opção inválida! Por favor, escolha uma operação válida."
        }
    else:
        return {
            "menu": "Choose a mathematical operation:",
            "somar": "1. Addition",
            "subtrair": "2. Subtract",
            "multiplicar": "3. Multiplication",
            "dividir": "4. Division",
            "sair": "0. Exit",
            "opcao": "Choose an option:",
            "primeiroNum": "Type the first number:",
            "segundoNum": "Type the second number:",
            "resultado": "The result is:",
            "resultadoAnterior": "Previous result:",
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

def solicitar_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Por favor, insira um número válido.")

def solicitar_opcao(mensagem):
    while True:
        opcao = input(mensagem)
        if opcao.isdigit():
            return opcao
        else:
            print("Erro: Por favor, escolha uma opção válida.")

def calcular(idioma):
    mensagens = traduzir(idioma)
    resultadoAnterior = None

    while True:
        print(f"\n{mensagens['resultadoAnterior']} {resultadoAnterior}")
        print(mensagens["menu"])
        print(mensagens["somar"])
        print(mensagens["subtrair"])
        print(mensagens["multiplicar"])
        print(mensagens["dividir"])
        print(mensagens["sair"])

        escolha = solicitar_opcao(mensagens["opcao"])
    
        if escolha == '0':
            print(mensagens["saida"])
            break
        
        num1 = solicitar_numero(mensagens["primeiroNum"])
        num2 = solicitar_numero(mensagens["segundoNum"])

        if escolha == '1':
            resultadoAnterior = somar(num1, num2)
            print(f"{mensagens['resultado']} {resultadoAnterior}")
        elif escolha == '2':
            resultadoAnterior = subtrair(num1, num2)
            print(f"{mensagens['resultado']} {resultadoAnterior}")
        elif escolha == '3':
            resultadoAnterior = multiplicar(num1, num2)
            print(f"{mensagens['resultado']} {resultadoAnterior}")
        elif escolha == '4':
            resultadoAnterior = dividir(num1, num2)
            print(f"{mensagens['resultado']} {resultadoAnterior}")
        else:
            print(mensagens["opcaoInvalida"])

if __name__ == "__main__":
    idioma = selecionar_idioma()
    calcular(idioma)
