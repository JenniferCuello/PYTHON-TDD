import pytest
from isbn_validator import es_isbn_valido

def test_isbn10_valido():
    isbn = "0471958697"
    assert es_isbn_valido(isbn) == True

def test_isbn13_valido():
    isbn = "9780470059029"  # ISBN de 13 dígitos válido
    assert es_isbn_valido(isbn) == True  # Esperamos que sea válido

def test_isbn13_invalido():
    isbn = "9780470059020"  # ISBN de 13 dígitos que no cumple la validación
    assert es_isbn_valido(isbn) == False  # Esperamos que sea inválido

def test_isbn_longitud_incorrecta():
    isbn = "123456789"  # ISBN de longitud incorrecta (9 dígitos)
    assert es_isbn_valido(isbn) == False  # Esperamos que sea inválido


def test_isbn_con_caracteres_especiales():
    isbn = "97804@5902!"  # Contiene caracteres especiales
    assert es_isbn_valido(isbn) == False  # Esperamos que sea inválido

def test_isbn10_con_X():
    isbn = "123456789X"  # ISBN de 10 dígitos válido con "X" como último dígito
    assert es_isbn_valido(isbn) == True  # Esperamos que sea válido
