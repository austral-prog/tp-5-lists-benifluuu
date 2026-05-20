def add_elements(lista):
    """
    Agrega el elemento 'Pink' al principio de la lista y 'Yellow' al final.
    Retorna la lista modificada.
    
    Parámetros:
    lista (list): La lista original de elementos.
    
    Retorna:
    list: La misma lista pero con las modificaciones aplicadas.
    """
    # 1. Insertamos 'Pink' en la posición 0 (al principio)
    lista.insert(0, 'Pink')
    
    # 2. Agregamos 'Yellow' al final de la lista
    lista.append('Yellow')
    
    # 3. Retornamos la lista ya modificada
    return lista