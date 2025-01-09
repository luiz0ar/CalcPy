import os

# Function to clear the terminal screen
def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to select the language
def selecionarIdioma():
    while True:
        print("\nCALCULATOR")
        print("Escolha o idioma / Choose the language / Elegir idioma:")  # Language selection prompt
        print("1. Português")
        print("2. English")
        print("3. Español")
        escolha = input("\n")  # User input for language selection

        # Language selection based on user input
        if escolha == '1':
            idioma = 'pt'  # Portuguese
            limparTela()  # Clear the screen
            print("Bem-vindo à Calculadora!")  # Welcome message in Portuguese
            return idioma
        elif escolha == '2':
            idioma = 'en'  # English
            limparTela()  # Clear the screen
            print("Welcome to the Calculator!")  # Welcome message in English
            return idioma
        elif escolha == '3':
            idioma = 'es'  # Spanish
            limparTela()  # Clear the screen
            print("¡Bienvenido a la Calculadora!")  # Welcome message in Spanish
            return idioma
        else:
            limparTela()  # Clear the screen for invalid input
            print("Opção inválida! Tente novamente. / Invalid option! Try again. / ¡Opción no válida! Intenta nuevamente.")  # Error message

# Function to return a dictionary with translated phrases based on the selected language
def traduzir(idioma):
    if idioma == 'pt':  # Portuguese translations
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
    elif idioma == 'en':  # English translations
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
    else:  # Spanish translations
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

# Mathematical operations
def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return None  # Return None if division by zero is attempted
    return x / y

# Function to request a valid number input from the user
def solicitarNum(mensagem):
    while True:
        try:
            return float(input(mensagem))  # Try to convert the input to a float
        except ValueError:
             print(traduzir(idioma)["numValido"])  # Show error message if input is invalid

# Function to request the user to select an operation
def solicitarOpcao(mensagem, mensagens):
    while True:
        print(mensagens["somar"])
        print(mensagens["subtrair"])
        print(mensagens["multiplicar"])
        print(mensagens["dividir"])
        print(mensagens["voltar"])
        print(mensagens["sair"])

        opcao = input(mensagem)  # User input for operation choice
        
        if opcao.isdigit() and 0 <= int(opcao) <= 5:  # Check if option is valid
            return opcao
        else:
            limparTela()  # Clear the screen if input is invalid
            print(mensagens["opcaoValida0a5"])  # Show error message for invalid option

# Main calculator function that manages operations and history
def calcular(idioma):
    while True:
        mensagens = traduzir(idioma)  # Get translated messages for the selected language
        resultados = []  # List to store results

        while True:
            if resultados:
                print(f"\n{mensagens['resultadoAnterior']}")  # Display previous results
                for res in resultados:
                    print(res)

            escolha = solicitarOpcao(mensagens["opcao"], mensagens)  # Get operation choice

            if escolha == '0':
                print(mensagens["saida"])  # Exit the calculator
                return
            elif escolha == '5':
                limparTela()  # Clear screen
                idioma = selecionarIdioma()  # Re-select language
                break
            else:
                num1 = solicitarNum(mensagens["primeiroNum"])  # Get first number
                num2 = solicitarNum(mensagens["segundoNum"])  # Get second number

                # Perform the selected operation and show the result
                if escolha == '1':
                    resultado = somar(num1, num2)
                    resultados.append(f"{num1} + {num2} = {resultado}")
                    limparTela()  # Clear the screen
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
                    if resultado is None:  # Handle division by zero
                        resultados.append(f"{num1} / {num2} = {mensagens['divisaoImpossivel']}")
                        limparTela()
                        print(f"\n{mensagens['divisaoImpossivel']}")
                    else:
                        resultados.append(f"{num1} / {num2} = {resultado}")
                        limparTela()
                        print(f"\n{mensagens['resultado']} {resultado}")
                else:
                    print(mensagens["opcaoInvalida"])  # Show error message for invalid operation

# Main entry point
if __name__ == "__main__":
    idioma = selecionarIdioma()  # Start by selecting the language
    calcular(idioma)  # Start the calculator
