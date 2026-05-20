def is_empty(lista):
    """
    Determina si una lista está vacía.

    Parámetros:
    lista (list): Una lista de elementos.

    Retorna:
    bool: True si la lista está vacía, False en caso contrario.
    """
    # Retornamos directamente el resultado de la comparación lógica.
    # Si la lista no tiene elementos, la igualdad dará True; si tiene algo, dará False.
    return lista == []