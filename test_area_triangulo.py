from app import calcular_area

def test_area_triangulo_correcto():
    assert calcular_area(5, 7) == 17.5

@pytest.mark.parametrize("b,h", [
    (-1,  5),
    ( 5, -1),
    (-1, -1),
])
def test_valores_negativos_error(b, h):
    """Inputs must be non-negative."""
    with pytest.raises(ValueError):
        calcular_area(b, h)

@pytest.mark.parametrize("b,h", [
    (0,  5),
    (5,  0),
    (0,  0),
])
def test_ceros_error(b, h):
    """Neither base nor height may be zero."""
    with pytest.raises(ValueError):
        calcular_area(b, h)