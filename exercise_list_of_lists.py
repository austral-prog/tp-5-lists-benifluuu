def list_of_lists(lista):
    """
    Recibe una lista con exactamente 3 listas internas y recorta cada una
    según las reglas de slicing estipuladas. Retorna la lista modificada.
    
    Parámetros:
    lista (list): Una lista que contiene 3 sublistas.
    
    Retorna:
    list: La lista con sus sublistas recortadas de forma segura.
    """
    # 1. Recortar la primera sublista (índices 0 y 1)
    sublista1_recortada = lista[0][:2]
    
    # 2. Recortar la segunda sublista (índices 1 al 3 inclusive)
    sublista2_recortada = lista[1][1:4]
    
    # 3. Recortar la tercera sublista (los últimos 2 elementos)
    sublista3_recortada = lista[2][-2:]
    
    # 4. Construimos y retornamos la nueva estructura unificada
    return [sublista1_recortada, sublista2_recortada, sublista3_recortada]