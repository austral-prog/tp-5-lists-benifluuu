def remove_elements(lista):
    """
    Remueve el primer elemento (índice 0), el quinto (índice 4) y el sexto (índice 5)
    de forma segura, soportando listas de cualquier tamaño.
    
    Parámetros:
    lista (list): La lista original.
    
    Retorna:
    list: La lista con las eliminaciones aplicadas.
    """
    
    # 1. Evaluamos el sexto elemento (índice 5)
    if len(lista) > 5:
        lista.pop(5)
        
    # 2. Evaluamos el quinto elemento (índice 4)
    if len(lista) > 4:
        lista.pop(4)
        
    # 3. Evaluamos el primer elemento (índice 0)
    if len(lista) > 0:
        lista.pop(0)
        
    return lista