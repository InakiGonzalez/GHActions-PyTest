from app import area_triangulo

def test_area_triangulo_correcto():
    assert area_triangulo.calcular_area(10, 5) == 25

def test_area_triangulo_incorrecto():
    assert area_triangulo.calcular_area(10, 5) == 20