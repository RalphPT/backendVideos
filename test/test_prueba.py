from prueba import sumar, dividir
import pytest

def test_sumar_exitoso():
    num1 = 5
    num2 = 4
    resultado =sumar(num1, num2)
    assert resultado == 9

def test_sumar_error():
    resultado = sumar('a','c')
    assert resultado == 'ac'

def test_dividir():
    with pytest.raises(ZeroDivisionError):
        resultado = dividir(10, 0)
        assert resultado == 0 #Con el pytest ya no será necesario colocar el assert, porque estamos capturando el error o testeando si en caso tuviéramos un error