def get_element(lista, indice):
    """
    Retorna el elemento de la lista en la posición indicada por el índice.
    Si el índice está fuera de rango, retorna None.
    
    Parámetros:
    lista (list): La lista de elementos.
    indice (int): El índice del elemento a obtener (puede ser positivo o negativo).
    
    Retorna:
    El elemento de la lista o None si el índice es inválido.
    """
    # 1. Obtener la longitud actual de la lista
    largo = len(lista)
    
    # 2. Validar si el índice está dentro del rango permitido (tanto positivo como negativo)
    if indice >= -largo and indice < largo:
        # Si es válido, retornamos el elemento de forma segura
        return lista[indice]
    else:
        # Si está fuera de rango, retornamos None
        return None