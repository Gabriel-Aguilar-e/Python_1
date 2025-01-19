class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

def menu():
    print("Gestion de contactos")
    print("1. Añadir contacto")
    print("2. Lista de contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("0. Salir\n")

contactos = []
while True:
    menu()
    opcion = input("Elige una opción: ")
    if opcion == '0':
        print("Saliendo del programa")
        break
    elif opcion == '1':
        print("")
        print("Añadir contacto")
        nombre = input("Ingrese el nombre: ")
        telefono = input("Ingrese el teléfono: ")
        contacto = Contacto(nombre, telefono)
        contactos.append(contacto)
        print("")
    elif opcion == '2':
        print("")
        print("Lista de contactos")
        for contacto in contactos:
            print(f"Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}\n")
    elif opcion == '3':
        print("")
        nombre = input("Ingrese el nombre a buscar: ")
        for contacto in contactos:
            if contacto.nombre == nombre:
                print(f"Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}\n")
    elif opcion == '4':
        print("")
        nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
        contacto_encontrado = False
        for contacto in contactos:
            if contacto.nombre == nombre:
                contactos.remove(contacto)
                contacto_encontrado = True
                print("")
                break
        if not contacto_encontrado:
            print("Contacto no encontrado\n")
    else:
        print("Opción no valida.")
        print("-------","Fin","-------\n")