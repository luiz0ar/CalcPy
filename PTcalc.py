# Importa o módulo os para poder executar comandos de sistema operacional.
import os

# Função para limpar a tela do terminal
def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')  # Executa 'cls' no Windows, ou 'clear' em sistemas Unix-like.

# Função para selecionar o idioma
def selecionarIdioma():
    while True:
        # Exibe o menu de idiomas
        print("\nCALCULATOR")
        print("Escolha o idioma / Choose the language / Elegir idioma:")
        print("1. Português")
        print("2. English")
        print("3. Español")
        escolha = input("\n")  # Solicita que o usuário escolha um idioma

        # Condicionais para verificar a escolha do usuário e retornar o idioma correspondente
        if escolha == '1':
            idioma = 'pt'
            limparTela()
            print("Bem-vindo à Calculadora!")  # Mensagem de boas-vindas em português
            return idioma
        elif escolha == '2':
            idioma = 'en'
            limparTela()
            print("Welcome to the Calculator!")  # Mensagem de boas-vindas em inglês
            return idioma
        elif escolha == '3':
            idioma = 'es'
            limparTela()
            print("¡Bienvenido a la Calculadora!")  # Mensagem de boas-vindas em espanhol
            return idioma
        else:
            limparTela()
            print("Opção inválida! Tente novamente. / Invalid option! Try again. / ¡Opción no válida! Intenta nuevamente.")  # Caso a opção não seja válida

# Função para traduzir os textos com base no idioma escolhido
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

# Funções de operações matemáticas
def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:  # Verifica se a divisão por zero foi tentada
        return None
    return x / y

# Função para solicitar um número do usuário, garantindo que seja um número válido
def solicitarNum(mensagem):
    while True:
        try:
            return float(input(mensagem))  # Tenta converter a entrada para float
        except ValueError:  # Se não for possível, exibe mensagem de erro
             print(traduzir(idioma)["numValido"])

# Função para solicitar a escolha de uma operação
def solicitarOpcao(mensagem, mensagens):
    while True:
        # Exibe as opções de operações disponíveis
        print(mensagens["somar"])
        print(mensagens["subtrair"])
        print(mensagens["multiplicar"])
        print(mensagens["dividir"])
        print(mensagens["voltar"])
        print(mensagens["sair"])

        opcao = input(mensagem)  # Solicita a opção ao usuário
        
        # Verifica se a opção é um número e está entre 0 e 5
        if opcao.isdigit() and 0 <= int(opcao) <= 5:
            return opcao
        else:
            limparTela()
            print(mensagens["opcaoValida0a5"])  # Mensagem de erro se a opção não for válida

# Função principal que executa o cálculo
def calcular(idioma):
    while True:
        mensagens = traduzir(idioma)  # Obtém as mensagens traduzidas para o idioma escolhido
        resultados = []  # Lista que armazenará os resultados das operações
        
        while True:
            if resultados:
                # Se houver resultados anteriores, exibe-os
                print(f"\n{mensagens['resultadoAnterior']}")
                for res in resultados:
                    print(res)

            # Solicita ao usuário escolher uma operação
            escolha = solicitarOpcao(mensagens["opcao"], mensagens)

            if escolha == '0':  # Se a opção for '0', sai da calculadora
                print(mensagens["saida"])
                return
            elif escolha == '5':  # Se a opção for '5', volta ao menu de seleção de idioma
                limparTela()
                idioma = selecionarIdioma()
                break
            else:
                # Solicita os dois números para a operação
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
                        # Se a divisão for impossível (divisão por zero), exibe uma mensagem de erro
                        resultados.append(f"{num1} / {num2} = {mensagens['divisaoImpossivel']}")
                        limparTela()
                        print(f"\n{mensagens['divisaoImpossivel']}")
                    else:
                        resultados.append(f"{num1} / {num2} = {resultado}")
                        limparTela()
                        print(f"\n{mensagens['resultado']} {resultado}")
                else:
                    print(mensagens["opcaoInvalida"])  # Caso a opção não seja válida

# Execução principal do programa
if __name__ == "__main__":
    idioma = selecionarIdioma()  # Solicita que o usuário selecione o idioma
    calcular(idioma)  # Inicia a calculadora com o idioma escolhido
