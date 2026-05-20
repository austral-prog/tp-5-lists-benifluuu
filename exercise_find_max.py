def find_max(lista):
    """
    Encuentra y retorna el valor máximo en una lista de números.
    Si la lista está vacía, retorna None.
    
    Parámetros:
    lista (list): Una lista de números enteros o decimales.
    
    Retorna:
    El número máximo presente en la lista o None si está vacía.
    """
    # 1. Validación de lista vacía
    if len(lista) == 0:
        return None
        
    # 2. Si tiene elementos, usamos la función max() de Python de forma segura
    return max(lista)