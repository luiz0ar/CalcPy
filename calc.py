def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Divisão não possível."
    return x / y

def calcular():
    while True:
        print("\nEscolha uma operação:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Sair")
        
        escolha = input("Escolha uma operação matemáica: ")

        if escolha == '0':
            print("Adeus...")
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"\nO resultado é: {somar(num1, num2)}")
        elif escolha == '2':
            print(f"\nO resultado é: {subtrair(num1, num2)}")
        elif escolha == '3':
            print(f"\nO resultadoé: {multiplicar(num1, num2)}")
        elif escolha == '4':
            print(f"\nO resultado é: {dividir(num1, num2)}")
        else:
            print("Opção inválida! Por favor, escolha uma operação válida.")

if __name__ == "__main__":
    calcular()
