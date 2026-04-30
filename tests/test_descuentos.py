import pytest
from app.descuentos import calcular_descuento


def test_descuento_exitoso():
    resultado = calcular_descuento(1000, 20)
    assert resultado == 800


def test_precio_negativo_error():
    with pytest.raises(ValueError):
        calcular_descuento(-1000, 20)


def test_descuento_cien_por_ciento_edge_case():
    resultado = calcular_descuento(1000, 100)
    assert resultado == 0