def mostrar_titulo(t):
    """Muestra por consola un encabezado de texto estético y enmarcado.
    Args:
        t (str): El texto del título a mostrar.
    """
    print("\n============================")
    print(t)
    print("============================")


def pedir_numero(mensaje):
    valor = input(mensaje)
    try:
        return int(valor)
    except ValueError:
        print("Número no válido. Se usará 0")
        return 0


def formatear_moneda(x):
    return str(round(x, 2)) + " €"
