def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b != 0:
        return a / b
    else:
        return print("Error, division por 0")

#Menú
def menu():
    print("Calculadora básica\n")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("0. Salir")

while True:
    menu()
    opcion = input("Elige una opción: ")
    if opcion == '0':
        print("")
        print("Saliendo del programa")
        break
    
    if opcion in ['1', '2', '3', '4']:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        if opcion == '1':
            print("")
            print(f"Resultado: {suma(num1, num2)}\n")
        if opcion == '2':
            print("")
            print(f"Resultado: {resta(num1, num2)}\n")
        if opcion == '3':
            print("")
            print(f"Resultado: {multiplicacion(num1, num2)}\n")
        if opcion == '4':
            print("")
            print(f"Resultado: {division(num1, num2)}\n")
    else:
        print("")
        print("Opción no valida.")
        print("-------","Fin","-------\n")
