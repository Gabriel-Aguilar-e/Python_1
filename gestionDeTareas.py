"""
5. Ejercicio Propuesto: Sistema de Gestión de Tareas
Objetivos :
• Aplicar el us o de clas es , lis tas , funciones y manejo de errores .
• Practicar la creación de un programa interactivo con múltiples
funcionalidades .
Des cripción del Ejercicio:
Des arrolla un s is tema de ges tión de tareas que permita al us uario añadir,
ver, bus car, actualizar y eliminar tareas . Cada tarea debe tener un título, una
des cripción y un es tado (pendiente o completada). El programa debe:
1. Permitir agregar nuevas tareas : Utiliza una clas e Tarea para
almacenar los detalles de cada tarea y guarda los objetos en una
lis ta.
2. Mos trar todas las tareas : Recorre la lis ta y mues tra los detalles de
cada tarea.
3. Bus car una tarea por título: Permite encontrar y mos trar información
de una tarea es pecífica.
4. Actualizar el es tado de una tarea: Permite cambiar el es tado de una
tarea a "completada".
5. Eliminar una tarea por título: Permite remover una tarea de la lis ta.
6. Manejar pos ibles errores (como ingres ar datos no válidos ): Utiliza
bloques try-except para manejar errores en las entradas .
7. Permitir al us uario realizar otra operación o salir del programa: Un
bucle while permite repetir el proceso has ta que el us uario decida
salir.
"""

class Tarea:
    def __init__(self, titulo, descripcion, estado):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

def menu():
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Buscar tarea")
    print("4. Actualizar tarea")
    print("5. Eliminar tarea")
    print("6. Salir\n")
    opcion = input("Seleccione una opción: ")
    return opcion
tareas = []

while True:
    opcion = menu()
    if opcion == '1':
        print("")
        try:
            titulo = input("Ingrese el título de la tarea: ").lower()
            descripcion = input("Ingrese la descripción de la tarea: ").lower()
            estado = input("Ingrese el estado de la tarea (pendiente o completada): ").lower()
            if estado not in ['pendiente', 'completada']:
                print("Estado no válido. Ingrese 'pendiente' o 'completada'.")
                continue
        except ValueError:
            print("Error, ingrese datos válidos (texto).")
        tarea = Tarea(titulo, descripcion, estado)
        tareas.append(tarea)
        print("Tarea agregada exitosamente.")
        print("")
    elif opcion == '2':
        print("")
        print("Tareas:\n")
        for tarea in tareas:
            print(f"Título: {tarea.titulo}, Descripción: {tarea.descripcion}, Estado: {tarea.estado}\n")
    elif opcion == '3':
        print("")
        try:
            titulo = input("Ingrese el título de la tarea a buscar: ")
            titulo = titulo.lower()
        except ValueError:
            print("Error, ingrese datos válidos (texto).")
        tarea_encontrada = False
        for tarea in tareas:
            if tarea.titulo == titulo:
                print(f"Título: {tarea.titulo}, Descripción: {tarea.descripcion}, Estado: {tarea.estado}\n")
                tarea_encontrada = True
                print("")
                break
        if not tarea_encontrada:
            print("Tarea no encontrada\n")
    elif opcion == '4':
        print("")
        try:
            titulo = input("Ingrese el título de la tarea que desea actualizar: ")
            titulo = titulo.lower()
        except ValueError:
            print("Error, ingrese datos válidos (texto).")
        tarea_encontrada = False
        for tarea in tareas:
            if tarea.titulo == titulo:
                estado = input("Ingrese el nuevo estado de la tarea (pendiente o completada): ")
                tarea.estado = estado
                print("")
                break
    elif opcion == '5':
        print("")
        try:
            titulo = input("Ingrese el título de la tarea que desea eliminar: ")
            titulo = titulo.lower()
        except ValueError:
            print("Error, ingrese datos válidos (texto).")
        tarea_encontrada = False
        for tarea in tareas:
            if tarea.titulo == titulo:
                tareas.remove(tarea)
                tarea_encontrada = True
                print("Tarea eliminada exitosamente.")
                print("")
                break
        if not tarea_encontrada:
            print("Tarea no encontrada\n")
    elif opcion == '6':
        print("-------","Fin","-------\n")
        break
    else:
        print("Opción no valida.")
        print("-------","Fin","-------\n")