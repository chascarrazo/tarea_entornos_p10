from clientes import clientes
from utilidades import pedir_numero

pedidos = []

def calcular_descuento_comercial(importe_total):
    """Aplica las reglas de negocio para determinar el descuento por volumen de compra.

    Args:
        importe_total (float): Suma total de los productos del pedido antes de aplicar impuestos.

    Returns:
        float: Cantidad económica a deducir  (10% si supera 100€, 5% si supera 50€).
    """
    if importe_total > 300:
        return importe_total * 0.15  # Linea nueva añadida
    elif importe_total > 100:
        return importe_total * 0.10
    elif importe_total > 50:
        return importe_total * 0.05
    return 0.0

def menu_pedidos():
    fin = False
    while fin is False:
        print("\n--- PEDIDOS ---")
        print("1. Crear pedido")
        print("2. Listar pedidos")
        print("3. Calcular total de un pedido")
        print("4. Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            nuevo_pedido()
        elif opcion == "2":
            ver_pedidos()
        elif opcion == "3":
            calcular_total_desde_menu()
        elif opcion == "4":
            fin = True
        else:
            print("Opción incorrecta")


def nuevo_pedido():
    """Gestiona el flujo guiado por consola para asociar un pedido a un cliente existente.

    Pide de forma iterativa las líneas de productos (comprobando que el nombre, cantidad
    y precio unitario sean válidos) y añade el pedido final a la lista global.
    """
    print("\nCREAR PEDIDO")
    if len(clientes) == 0:
        print("Primero debes crear un cliente")
        return

    i = 0
    while i < len(clientes):
        print(str(i + 1) + ". " + clientes[i]["nombre"])
        i = i + 1

    numero_cliente = pedir_numero("Elige cliente: ")
    if numero_cliente < 1 or numero_cliente > len(clientes):
        print("Cliente incorrecto")
        return

    lineas = []
    seguir = "s"
    while seguir == "s":
        producto = input("Producto: ")
        cantidad = pedir_numero("Cantidad: ")
        precio = float(input("Precio unidad: "))

        if producto == "":
            print("Producto vacío")
        elif cantidad <= 0:
            print("Cantidad incorrecta")
        elif precio <= 0:
            print("Precio incorrecto")
        else:
            lineas.append({"producto": producto, "cantidad": cantidad, "precio": precio})
            print("Línea añadida")

        seguir = input("¿Añadir otro producto? s/n: ")

    pedido = {"cliente": clientes[numero_cliente - 1], "lineas": lineas, "estado": "pendiente"}
    pedidos.append(pedido)
    print("Pedido creado")


def ver_pedidos():
    print("\nLISTADO DE PEDIDOS")
    if len(pedidos) == 0:
        print("No hay pedidos")
    else:
        pos = 0
        for p in pedidos:
            total = 0
            for linea in p["lineas"]:
                total = total + linea["cantidad"] * linea["precio"]
            descuento = calcular_descuento_comercial(total)
            total = total - descuento
            nom_cli = p["cliente"]["nombre"]
            est = p["estado"]
            tot_formateado = round(total, 2)
            print(f"{pos + 1}. Cliente: {nom_cli} | Estado: {est} | Total: {tot_formateado} €")
            pos = pos + 1


def calcular_total_desde_menu():
    if len(pedidos) == 0:
        print("No hay pedidos")
        return

    n = pedir_numero("Número de pedido: ")
    if n < 1 or n > len(pedidos):
        print("Pedido no válido")
        return

    p = pedidos[n - 1]
    suma = 0
    for linea in p["lineas"]:
        suma = suma + linea["cantidad"] * linea["precio"]

    descuento = calcular_descuento_comercial(suma)

    iva = (suma - descuento) * 0.21
    total = suma - descuento + iva

    print("Subtotal: " + str(round(suma, 2)))
    print("Descuento: " + str(round(descuento, 2)))
    print("IVA: " + str(round(iva, 2)))
    print("TOTAL: " + str(round(total, 2)))


def cambiar_estado_pedido():
    # Función sin usar, pensada para detectar código muerto o incompleto
    x = input("Nuevo estado: ")
    return x
