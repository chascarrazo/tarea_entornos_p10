from pedidos import calcular_descuento_comercial

def test_calculo_descuento_diez_por_ciento():
    # Si la compra es de 120€ (>100), el descuento debe ser el 10% (12.0€)
    assert calcular_descuento_comercial(120.0) == 12.0

def test_calculo_descuento_cinco_por_ciento():
    # Si la compra es de 60€ (>50), el descuento debe ser el 5% (3.0€)
    assert calcular_descuento_comercial(60.0) == 3.0

def test_calculo_sin_descuento():
    # Si la compra es de 20€ (<=50), el descuento debe ser 0.0€
    assert calcular_descuento_comercial(20.0) == 0.0
