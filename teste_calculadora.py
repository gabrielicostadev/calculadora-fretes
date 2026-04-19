import pytest
from calculadora import calcular_frete, TABELA_CONTEINER

def test_frete_5_eixos_sem_adicional():
    r = calcular_frete(100, 5)
    assert r["frete_base"] == round((100 * 66.765) + 625.16, 2)

def test_frete_7_eixos_com_adicional():
    r = calcular_frete(500, 7, 10)
    assert r["frete_final"] == round(r["frete_base"] * 1.10, 2)

def test_adicional_zero():
    r = calcular_frete(200, 6, 0)
    assert r["frete_final"] == r["frete_base"]

def test_distancia_invalida():
    with pytest.raises(ValueError):
        calcular_frete(0, 5)

def test_eixos_invalido():
    with pytest.raises(ValueError):
        calcular_frete(100, 8)  # 8 não existe na tabela

def test_percentual_negativo():
    with pytest.raises(ValueError):
        calcular_frete(100, 5, -10)