def find_min(lista):
    """
    Encuentra y retorna el valor mínimo en una lista de números.
    Si la lista está vacía, retorna None.
    
    Parámetros:
    lista (list): Una lista de números enteros o decimales.
    
    Retorna:
    El número mínimo presente en la lista o None si está vacía.
    """
    # 1. Validación preventiva para listas vacías
    if len(lista) == 0:
        return None
        
    # 2. Si contiene elementos, usamos la función min() de forma segura
    return min(lista)