def es_isbn_valido(isbn):
    if len(isbn) == 10:
        # Permitir "X" solo en la última posición, que representa el número 10
        if isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == 'X'):
            suma = sum((10 - i) * (int(d) if d != 'X' else 10) for i, d in enumerate(isbn))
            return suma % 11 == 0
    elif len(isbn) == 13 and isbn.isdigit():
        suma = sum((1 if i % 2 == 0 else 3) * int(d) for i, d in enumerate(isbn))
        return suma % 10 == 0
    return False  # Devuelve False si no cumple las condiciones
