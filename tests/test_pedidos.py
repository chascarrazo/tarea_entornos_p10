from pedidos import calcular_descuento_comercial


def test_calculo_descuento_quince_por_ciento():
    # Comprueba el tramo premium: 400€ (>300) debe aplicar el 15% -> 60.0€
    assert calcular_descuento_comercial(400.0) == 60.0

def test_calculo_descuento_diez_por_ciento():
    # Comprueba tramo alto: 120€ (>100) debe aplicar el 10% -> 12.0€
    assert calcular_descuento_comercial(120.0) == 12.0

def test_calculo_descuento_cinco_por_ciento():
    # Comprueba tramo medio: 60€ (>50) debe aplicar el 5% -> 3.0€
    assert calcular_descuento_comercial(60.0) == 3.0

def test_calculo_sin_descuento():
    # Comprueba sin tramo: 20€ (<=50) debe dar 0.0€
    assert calcular_descuento_comercial(20.0) == 0.0
