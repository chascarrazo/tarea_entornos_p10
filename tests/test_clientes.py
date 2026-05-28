from clientes import clientes, crear_cliente, validar_email

def test_validar_email_correcto():
    # Comprueba que un email con formato correcto devuelve True
    assert validar_email("alumno@instituto.es") is True

def test_validar_email_incorrecto():
    # Comprueba que un email sin arroba o punto devuelve False
    assert validar_email("correo-mal") is False