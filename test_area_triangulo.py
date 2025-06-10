from app import calcular_area

def test_area_triangulo_correcto():
    assert calcular_area(10, 5) == 25

def test_area_triangulo_incorrecto():
    assert calcular_area(10, 3) != 20