def check_lists(lista1, lista2):
    """
    Verifica si ambas listas tienen el mismo elemento en la tercera posición (índice 2).
    Retorna False si alguna lista es demasiado corta.
    
    Parámetros:
    lista1 (list): La primera lista a comparar.
    lista2 (list): La segunda lista a comparar.
    
    Retorna:
    bool: True si comparten el mismo elemento en el índice 2, False en caso contrario.
    """
    # 1. Validar que ambas listas contengan al menos 3 elementos
    if len(lista1) >= 3 and len(lista2) >= 3:
        # 2. Si son válidas, comparamos los elementos situados en el índice 2
        return lista1[2] == lista2[2]
    else:
        # Si alguna lista tiene menos de 3 elementos, no se puede evaluar el índice 2
        return False