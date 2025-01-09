import os

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def selecionarIdioma():
    while True:
        print("\nCALCULATOR")
        print("Escolha o idioma / Choose the language / Elegir idioma:")
        print("1. Português")
        print("2. English")
        print("3. Español")
        escolha = input("\n")

        if escolha == '1':
            idioma = 'pt'
            limparTela()
            return idioma
        elif escolha == '2':
            idioma = 'en'
            limparTela()
            return idioma
        elif escolha == '3':
            idioma = 'es'
            limparTela()
            return idioma
        else:
            limparTela()
            print("Opção inválida! Tente novamente. / Invalid option! Try again.")

def traduzir(idioma):
    if idioma == 'pt':
        return {
            "menu": "Escolha uma operação:",
            "somar": "1. Somar",
            "subtrair": "2. Subtrair",
            "multiplicar": "3. Multiplicar",
            "dividir": "4. Dividir",
            "voltar": "5. Voltar",
            "sair": "0. Sair",
            "opcao": "Escolha uma opção:",
            "primeiroNum": "Digite o primeiro número:",
            "segundoNum": "Digite o segundo número:",
            "resultado": "O resultado é:",
            "resultadoAnterior": "Resultado anterior:",
            "saida": "Saindo...",
            "opcaoInvalida": "Opção inválida! Por favor, escolha uma operação válida.",
            "divisaoImpossivel": "Divisão impossível.",
            "erroNumero": "Erro: Por favor, insira um número válido.",
            "erroOpcao": "Erro: Por favor, escolha uma opção válida de 0 a 5."
        }
    elif idioma == 'en':
        return {
            "menu": "Choose a mathematical operation:",
            "somar": "1. Addition",
            "subtrair": "2. Subtract",
            "multiplicar": "3. Multiplication",
            "dividir": "4. Division",
            "voltar": "5. Back",
            "sair": "0. Exit",
            "opcao": "Choose an option:",
            "primeiroNum": "Type the first number:",
            "segundoNum": "Type the second number:",
            "resultado": "The result is:",
            "resultadoAnterior": "Previous result:",
            "saida": "Leaving...",
            "opcaoInvalida": "Invalid Option! Please choose a valid operation.",
            "divisaoImpossivel": "Impossible division.",
            "erroNumero": "Error: Please enter a valid number.",
            "erroOpcao": "Error: Please choose a valid option from 0 to 5."
        }
    else:
        return {
            "menu": "Elige una operación:",
            "somar": "1. Sumar",
            "subtrair": "2. Restar",
            "multiplicar": "3. Multiplicar",
            "dividir": "4. Dividir",
            "voltar": "5. Volver",
            "sair": "0. Salir",
            "opcao": "Elige una opción:",
            "primeiroNum": "Introduce el primer número:",
            "segundoNum": "Introduce el segundo número:",
            "resultado": "El resultado es:",
            "resultadoAnterior": "Resultado anterior:",
            "saida": "Partida...",
            "opcaoInvalida": "¡Opción no válida! Por favor, elija una operación válida.",
            "divisaoImpossivel": "División imposible.",
            "erroNumero": "Error: Por favor, ingrese un número válido.",
            "erroOpcao": "Error: Por favor, elija una opción válida de 0 a 5."
        }

def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return None
    return x / y

def solicitarNum(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print(mensagem)  # Mensagem de erro no idioma selecionado

def solicitarOpcao(mensagem):
    while True:
        opcao = input(mensagem)
        if opcao.isdigit() and opcao in ['0', '1', '2', '3', '4', '5']:
            return opcao
        else:
            print(mensagem)  # Mensagem de erro no idioma selecionado

def calcular(idioma):
    mensagens = traduzir(idioma)
    resultadoAnterior = None

    while True:
        if resultadoAnterior is not None:
            print(f"\n{mensagens['resultadoAnterior']} {resultadoAnterior}")
        print(mensagens["menu"])
        print(mensagens["somar"])
        print(mensagens["subtrair"])
        print(mensagens["multiplicar"])
        print(mensagens["dividir"])
        print(mensagens["voltar"])
        print("")
        print(mensagens["sair"])

        escolha = solicitarOpcao(mensagens["opcao"])

        if escolha == '0':
            print(mensagens["saida"])
            break
        elif escolha == '5':
            limparTela()
            continue
        else:
            num1 = solicitarNum(mensagens["primeiroNum"])
            num2 = solicitarNum(mensagens["segundoNum"])

            if escolha == '1':
                resultadoAnterior = somar(num1, num2)
                limparTela()
                print(f"\n{mensagens['resultado']} {resultadoAnterior}")
            elif escolha == '2':
                resultadoAnterior = subtrair(num1, num2)
                limparTela()
                print(f"\n{mensagens['resultado']} {resultadoAnterior}")
            elif escolha == '3':
                resultadoAnterior = multiplicar(num1, num2)
                limparTela()
                print(f"\n{mensagens['resultado']} {resultadoAnterior}")
            elif escolha == '4':
                resultadoAnterior = dividir(num1, num2)
                limparTela()
                if resultadoAnterior is None:
                    print(f"\n{mensagens['divisaoImpossivel']}")
                else:
                    print(f"\n{mensagens['resultado']} {resultadoAnterior}")
            else:
                print(mensagens["opcaoInvalida"])

if __name__ == "__main__":
    idioma = selecionarIdioma()
    calcular(idioma)
