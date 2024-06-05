# -*- coding: utf-8 -*-
# Gestión de Contactos

contactos = {}  # Diccionario para almacenar los contactos

def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    numero_telefono = input("Ingrese el número de teléfono: ")
    contactos[nombre] = numero_telefono
    print("Contacto agregado correctamente.")

def buscar_contacto():
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    if nombre in contactos:
        print(f"El número de teléfono de {nombre} es: {contactos[nombre]}")
    else:
        print(f"El contacto {nombre} no se encuentra en la lista.")

def mostrar_contactos():
    if contactos:
        print("Contactos:")
        for nombre, numero_telefono in contactos.items():
            print(f"- {nombre}: {numero_telefono}")
    else:
        print("La lista de contactos está vacía.")

def actualizar_numero_telefono():
    nombre = input("Ingrese el nombre del contacto a actualizar: ")
    if nombre in contactos:
        nuevo_numero_telefono = input("Ingrese el nuevo número de teléfono: ")
        contactos[nombre] = nuevo_numero_telefono
        print(f"El número de teléfono de {nombre} ha sido actualizado correctamente.")
    else:
        print(f"El contacto {nombre} no se encuentra en la lista.")

def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in contactos:
        del contactos[nombre]
        print(f"El contacto {nombre} ha sido eliminado correctamente.")
    else:
        print(f"El contacto {nombre} no se encuentra en la lista.")

def salir():
    print("¡Hasta luego!")

# Bucle principal del programa
while True:
    print("\nBienvenido al sistema de gestión de contactos.")
    print("Opciones:")
    print("1. Agregar un contacto")
    print("2. Buscar un contacto")
    print("3. Mostrar todos los contactos")
    print("4. Actualizar número de teléfono")
    print("5. Eliminar un contacto")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        buscar_contacto()
    elif opcion == "3":
        mostrar_contactos()
    elif opcion == "4":
        actualizar_numero_telefono()
    elif opcion == "5":
        eliminar_contacto()
    elif opcion == "6":
        salir()
        break
    else:
        print("Opción no válida. Por favor, intenta nuevamente.")
