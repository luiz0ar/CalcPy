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
            print("Bem-vindo à Calculadora!")
            return idioma
        elif escolha == '2':
            idioma = 'en'
            limparTela()
            print("Welcome to the Calculator!")
            return idioma
        elif escolha == '3':
            idioma = 'es'
            limparTela()
            print("¡Bienvenido a la Calculadora!")
            return idioma
        else:
            limparTela()
            print("Opção inválida! Tente novamente. / Invalid option! Try again. / ¡Opción no válida! Intenta nuevamente.")

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
            "resultadoAnterior": "Resultados anteriores:",
            "saida": "Saindo...",
            "opcaoInvalida": "Opção inválida! Por favor, escolha uma operação válida.",
            "divisaoImpossivel": "Divisão impossível.",
            "opcaoValida0a5": "Opção inválida! Por favor, escolha uma opção válida entre 0 e 5.",
            "numValido": "Opção inválida! Por favor, insira um número válido.",
            "historico": "Histórico de resultados:"
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
            "resultadoAnterior": "Previous results:",
            "saida": "Leaving...",
            "opcaoInvalida": "Invalid Option! Please choose a valid operation.",
            "divisaoImpossivel": "Impossible division.",
            "opcaoValida0a5": "Invalid option! Please choose a valid option between 0 and 5.",
            "numValido": "Invalid option! Please enter a valid number.",
            "historico": "History of results:"
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
            "resultadoAnterior": "Resultados anteriores:",
            "saida": "Partida...",
            "opcaoInvalida": "¡Opción no válida! Por favor, elija una operación válida.",
            "divisaoImpossivel": "División imposible.",
            "opcaoValida0a5": "¡Opción no válida! Por favor, elija una opción válida entre 0 y 5.",
            "numValido": "¡Opción no válida! Por favor, introduce un número válido.",
            "historico": "Historial de resultados:"
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
             print(traduzir(idioma)["numValido"])

def solicitarOpcao(mensagem, mensagens):
    while True:
        print(mensagens["somar"])
        print(mensagens["subtrair"])
        print(mensagens["multiplicar"])
        print(mensagens["dividir"])
        print(mensagens["voltar"])
        print(mensagens["sair"])

        opcao = input(mensagem)
        
        if opcao.isdigit() and 0 <= int(opcao) <= 5:
            return opcao
        else:
            limparTela()
            print(mensagens["opcaoValida0a5"])

def calcular(idioma):
    while True:
        mensagens = traduzir(idioma)
        resultados = []  # Lista para armazenar os resultados temporariamente
        
        while True:
            # Exibe todos os resultados anteriores no idioma atual
            if resultados:
                print(f"\n{mensagens['resultadoAnterior']}")
                for res in resultados:
                    print(res)

            escolha = solicitarOpcao(mensagens["opcao"], mensagens)

            if escolha == '0':
                print(mensagens["saida"])
                return
            elif escolha == '5':
                limparTela()
                idioma = selecionarIdioma()
                break
            else:
                num1 = solicitarNum(mensagens["primeiroNum"])
                num2 = solicitarNum(mensagens["segundoNum"])

                if escolha == '1':
                    resultado = somar(num1, num2)
                    resultados.append(f"{num1} + {num2} = {resultado}")
                    limparTela()
                    print(f"\n{mensagens['resultado']} {resultado}")
                elif escolha == '2':
                    resultado = subtrair(num1, num2)
                    resultados.append(f"{num1} - {num2} = {resultado}")
                    limparTela()
                    print(f"\n{mensagens['resultado']} {resultado}")
                elif escolha == '3':
                    resultado = multiplicar(num1, num2)
                    resultados.append(f"{num1} * {num2} = {resultado}")
                    limparTela()
                    print(f"\n{mensagens['resultado']} {resultado}")
                elif escolha == '4':
                    resultado = dividir(num1, num2)
                    if resultado is None:
                        resultados.append(f"{num1} / {num2} = {mensagens['divisaoImpossivel']}")
                        limparTela()
                        print(f"\n{mensagens['divisaoImpossivel']}")
                    else:
                        resultados.append(f"{num1} / {num2} = {resultado}")
                        limparTela()
                        print(f"\n{mensagens['resultado']} {resultado}")
                else:
                    print(mensagens["opcaoInvalida"])

if __name__ == "__main__":
    idioma = selecionarIdioma()
    calcular(idioma)
