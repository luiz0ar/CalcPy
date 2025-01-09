def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

def calcular():
    while True:
        print("\nEscolha uma operação:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")
        
        escolha = input("Digite o número da operação desejada: ")

        if escolha == '5':
            print("Saindo...")
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"O resultado de {num1} + {num2} é: {somar(num1, num2)}")
        elif escolha == '2':
            print(f"O resultado de {num1} - {num2} é: {subtrair(num1, num2)}")
        elif escolha == '3':
            print(f"O resultado de {num1} * {num2} é: {multiplicar(num1, num2)}")
        elif escolha == '4':
            print(f"O resultado de {num1} / {num2} é: {dividir(num1, num2)}")
        else:
            print("Opção inválida! Por favor, escolha uma operação válida.")

if __name__ == "__main__":
    calcular()
