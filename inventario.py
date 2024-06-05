# -*- coding: utf-8 -*-
# Inventario de la Tienda

inventario = {}  # Diccionario para almacenar los productos

def agregar_producto():
    nombre = input("Ingresa el nombre del producto: ")
    try:
        cantidad = int(input(f"Ingresa la cantidad de {nombre}: "))
        if nombre in inventario:
            inventario[nombre] += cantidad
        else:
            inventario[nombre] = cantidad
        print(f"Producto {nombre} agregado al inventario.")
    except ValueError:
        print("Por favor, ingresa una cantidad válida.")

def vender_producto():
    nombre = input("Ingresa el nombre del producto a vender: ")
    if nombre in inventario:
        try:
            cantidad = int(input(f"Ingresa la cantidad a vender de {nombre}: "))
            if cantidad <= inventario[nombre]:
                inventario[nombre] -= cantidad
                print("Venta realizada.")
                if inventario[nombre] == 0:
                    del inventario[nombre]
            else:
                print("No hay suficiente stock.")
        except ValueError:
            print("Por favor, ingresa una cantidad válida.")
    else:
        print(f"No se encontró el producto {nombre}.")

def mostrar_inventario():
    if inventario:
        print("Inventario:")
        for nombre, cantidad in inventario.items():
            print(f"- {nombre}: {cantidad}")
    else:
        print("El inventario está vacío.")

def salir():
    print("¡Hasta luego!")

# Bucle principal del programa
while True:
    print("\nBienvenido al sistema de inventario de la tienda.")
    print("Opciones:")
    print("1. Agregar un producto al inventario")
    print("2. Vender un producto")
    print("3. Mostrar inventario")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        vender_producto()
    elif opcion == "3":
        mostrar_inventario()
    elif opcion == "4":
        salir()
        break
    else:
        print("Opción no válida. Por favor, intenta nuevamente.")
