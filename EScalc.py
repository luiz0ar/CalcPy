# Importa el módulo os para poder ejecutar comandos del sistema operativo.
import os

# Función para limpiar la pantalla del terminal
def limpiarTela():
    os.system('cls' if os.name == 'nt' else 'clear')  # Ejecuta 'cls' en Windows o 'clear' en sistemas Unix-like.

# Función para seleccionar el idioma
def seleccionarIdioma():
    while True:
        # Muestra el menú de idiomas
        print("\nCALCULATOR")
        print("Escoge el idioma / Choose the language / Elegir idioma:")
        print("1. Portugués")
        print("2. Inglés")
        print("3. Español")
        eleccion = input("\n")  # Solicita al usuario que elija un idioma

        # Condicionales para verificar la elección del usuario y devolver el idioma correspondiente
        if eleccion == '1':
            idioma = 'pt'
            limpiarTela()
            print("¡Bienvenido a la Calculadora!")  # Mensaje de bienvenida en portugués
            return idioma
        elif eleccion == '2':
            idioma = 'en'
            limpiarTela()
            print("Welcome to the Calculator!")  # Mensaje de bienvenida en inglés
            return idioma
        elif eleccion == '3':
            idioma = 'es'
            limpiarTela()
            print("¡Bienvenido a la Calculadora!")  # Mensaje de bienvenida en español
            return idioma
        else:
            limpiarTela()
            print("¡Opción no válida! Intenta de nuevo. / Invalid option! Try again. / Opción no válida! Intenta nuevamente.")  # Si la opción no es válida

# Función para traducir los textos según el idioma elegido
def traducir(idioma):
    if idioma == 'pt':
        return {
            "menu": "Escoge una operación:",
            "somar": "1. Sumar",
            "subtrair": "2. Restar",
            "multiplicar": "3. Multiplicar",
            "dividir": "4. Dividir",
            "voltar": "5. Volver",
            "sair": "0. Salir",
            "opcao": "Escoge una opción:",
            "primeiroNum": "Introduce el primer número:",
            "segundoNum": "Introduce el segundo número:",
            "resultado": "El resultado es:",
            "resultadoAnterior": "Resultados anteriores:",
            "saida": "Saliendo...",
            "opcaoInvalida": "¡Opción no válida! Por favor, escoge una operación válida.",
            "divisaoImpossivel": "División imposible.",
            "opcaoValida0a5": "¡Opción no válida! Por favor, escoge una opción válida entre 0 y 5.",
            "numValido": "¡Opción no válida! Por favor, ingresa un número válido.",
            "historico": "Historial de resultados:"
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
            "saida": "Saliendo...",
            "opcaoInvalida": "¡Opción no válida! Por favor, elige una operación válida.",
            "divisaoImpossivel": "División imposible.",
            "opcaoValida0a5": "¡Opción no válida! Por favor, elige una opción válida entre 0 y 5.",
            "numValido": "¡Opción no válida! Por favor, introduce un número válido.",
            "historico": "Historial de resultados:"
        }

# Funciones para realizar las operaciones matemáticas
def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:  # Verifica si se intenta una división por cero
        return None
    return x / y

# Función para solicitar un número al usuario, asegurándose de que sea válido
def solicitarNum(mensaje):
    while True:
        try:
            return float(input(mensaje))  # Intenta convertir la entrada en un número flotante
        except ValueError:  # Si no es posible, muestra un mensaje de error
             print(traducir(idioma)["numValido"])

# Función para solicitar la opción de operación al usuario
def solicitarOpcao(mensaje, mensajes):
    while True:
        # Muestra las opciones de operaciones disponibles
        print(mensajes["somar"])
        print(mensajes["subtrair"])
        print(mensajes["multiplicar"])
        print(mensajes["dividir"])
        print(mensajes["voltar"])
        print(mensajes["sair"])

        opcion = input(mensaje)  # Solicita la opción al usuario
        
        # Verifica si la opción es un número y está entre 0 y 5
        if opcion.isdigit() and 0 <= int(opcion) <= 5:
            return opcion
        else:
            limpiarTela()
            print(mensajes["opcaoValida0a5"])  # Mensaje de error si la opción no es válida

# Función principal para ejecutar los cálculos
def calcular(idioma):
    while True:
        mensajes = traducir(idioma)  # Obtiene los mensajes traducidos al idioma elegido
        resultados = []  # Lista para almacenar los resultados de las operaciones
        
        while True:
            if resultados:
                # Si hay resultados anteriores, los muestra
                print(f"\n{mensajes['resultadoAnterior']}")
                for res in resultados:
                    print(res)

            # Solicita al usuario que elija una operación
            eleccion = solicitarOpcao(mensajes["opcao"], mensajes)

            if eleccion == '0':  # Si la opción es '0', sale de la calculadora
                print(mensajes["saida"])
                return
            elif eleccion == '5':  # Si la opción es '5', vuelve al menú de selección de idioma
                limpiarTela()
                idioma = seleccionarIdioma()
                break
            else:
                # Solicita los dos números para la operación
                num1 = solicitarNum(mensajes["primeiroNum"])
                num2 = solicitarNum(mensajes["segundoNum"])

                if eleccion == '1':
                    resultado = somar(num1, num2)
                    resultados.append(f"{num1} + {num2} = {resultado}")
                    limpiarTela()
                    print(f"\n{mensajes['resultado']} {resultado}")
                elif eleccion == '2':
                    resultado = subtrair(num1, num2)
                    resultados.append(f"{num1} - {num2} = {resultado}")
                    limpiarTela()
                    print(f"\n{mensajes['resultado']} {resultado}")
                elif eleccion == '3':
                    resultado = multiplicar(num1, num2)
                    resultados.append(f"{num1} * {num2} = {resultado}")
                    limpiarTela()
                    print(f"\n{mensajes['resultado']} {resultado}")
                elif eleccion == '4':
                    resultado = dividir(num1, num2)
                    if resultado is None:
                        # Si la división es imposible (división por cero), muestra un mensaje de error
                        resultados.append(f"{num1} / {num2} = {mensajes['divisaoImpossivel']}")
                        limpiarTela()
                        print(f"\n{mensajes['divisaoImpossivel']}")
                    else:
                        resultados.append(f"{num1} / {num2} = {resultado}")
                        limpiarTela()
                        print(f"\n{mensajes['resultado']} {resultado}")
                else:
                    print(mensajes["opcaoInvalida"])  # Si la opción no es válida

# Ejecución principal del programa
if __name__ == "__main__":
    idioma = seleccionarIdioma()  # Solicita al usuario que seleccione el idioma
    calcular(idioma)  # Inicia la calculadora con el idioma elegido
