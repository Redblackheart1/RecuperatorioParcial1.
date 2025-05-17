# Gestión de Stock - Recuperatorio Parcial 1

# Listas paralelas
nombres = []
cantidades = []

# Menú principal
while True:
    print("\n🛒 Menú de opciones:")
    print("1. Agregar producto")
    print("2. Ver productos agotados")
    print("3. Actualizar stock")
    print("4. Ver todos los productos")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        try:
            cantidad = int(input("Ingrese la cantidad en stock: "))
            nombres.append(nombre)
            cantidades.append(cantidad)
            print("✅ Producto agregado con éxito.")
        except ValueError:
            print("❌ Error: La cantidad debe ser un número entero.")

    elif opcion == "2":
        agotados = False
        print("📦 Productos agotados:")
        for i in range(len(nombres)):
            if cantidades[i] == 0:
                print("-", nombres[i])
                agotados = True
        if not agotados:
            print("✅ No hay productos agotados.")

    elif opcion == "3":
        producto = input("Ingrese el nombre del producto a actualizar: ")
        if producto in nombres:
            index = nombres.index(producto)
            try:
                nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                cantidades[index] = nueva_cantidad
                print("✅ Stock actualizado correctamente.")
            except ValueError:
                print("❌ Error: La cantidad debe ser un número entero.")
        else:
            print("❌ Producto no encontrado.")

    elif opcion == "4":
        print("📋 Listado de productos:")
        for i in range(len(nombres)):
            print(f"{nombres[i]} - {cantidades[i]} unidades")

    elif opcion == "5":
        print("👋 Gracias por usar el sistema.")
        break

    else:
        print("❌ Opción inválida. Intente nuevamente.")