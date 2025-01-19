"""
Proyecto 3: Sistema de Inventario
Objetivos :
• Aplicar el us o de clas es , lis tas , módulos y manejo de errores .
• Des arrollar una aplicación más compleja con múltiples
funcionalidades .
Ejercicio:
Crea un s is tema de inventario para una tienda. El programa debe:
1. Permitir agregar nuevos productos (nombre, cantidad,
precio): Utiliza una clas e Pr oduct o y almacena objetos en una lis ta.
2. Mos trar todos los productos : Recorre la lis ta y mues tra los detalles
de cada producto.
3. Bus car un producto por nombre: Permite encontrar y mos trar
información de un producto es pecífico.
4. Actualizar la cantidad de un producto: Permite modificar la cantidad
de un producto exis tente.
5. Eliminar un producto: Permite remover un producto de la lis ta.
6. Manejar pos ibles errores (como ingres ar datos no válidos ): Utiliza
bloques try-except para manejar errores en las entradas .
7. Permitir al us uario realizar otra operación o salir del programa: Un
bucle while permite repetir el proces o has ta que el us uario decida
salir.
"""

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

def menu():
    print("Sistema de inventario")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Actualizar cantidad")
    print("5. Eliminar producto")
    print("0. Salir\n")

inventario = []

while True:
    menu()
    opcion = input("Elige una opción: ")
    if opcion == '0':
        print("Saliendo del programa\n")
        break
    elif opcion == '1':
        print("")
        print("Agregar un producto:\n")
        try:
            nombre = input("Ingrese el nombre: ").lower()
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
        except ValueError:
            print("Error, ingrese datos válidos (texto, cantidad entera, número con o sin decimal).")
            continue
        producto = Producto(nombre, cantidad, precio)
        inventario.append(producto)
        print("Producto agregado exitosamente.")
        print("")
    elif opcion == '2':
        print("")
        print("Inventario:\n")
        for producto in inventario:
            print(f"Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}\n")
    elif opcion == '3':
        print("")
        try:
            nombre = input("Ingrese el nombre a buscar: \n")
            nombre = nombre.lower()
        except ValueError:
            print("Error, ingrese datos válidos (texto).")
        for producto in inventario:
            if producto.nombre == nombre:
                print(f"Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}\n")
    elif opcion == '4':
        print("")
        try:
            nombre = input("Ingrese el nombre del producto que desea actualizar: ")
            nombre = nombre.lower()
        except ValueError:
            print("Error, ingrese datos válidos (texto).")
        for producto in inventario:
            if producto.nombre == nombre:
                cantidad = int(input("Ingrese la nueva cantidad: "))
                producto.cantidad = cantidad
                print("")
                break
    elif opcion == '5':
        print("")
        try:
            nombre = input("Ingrese el nombre del producto que desea eliminar: ")
            nombre = nombre.lower()
        except ValueError:
            print("Error, ingrese datos válidos (texto).")
        producto_encontrado = False
        for producto in inventario:
            if producto.nombre == nombre:
                inventario.remove(producto)
                producto_encontrado = True
                print("")
                break
        if not producto_encontrado:
            print("Producto no encontrado\n")
    else:
        print("")
        print("Opción no valida.")
        print("-------","Fin","-------\n")