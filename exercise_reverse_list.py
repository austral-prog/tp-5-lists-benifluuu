def reverse_list(lista):
    """
    Retorna una nueva lista con los elementos en orden inverso.
    La lista original no es modificada.
    
    Parámetros:
    lista (list): La lista original.
    
    Retorna:
    list: Una copia de la lista en orden inverso.
    """
    # El slicing [:: -1] genera una nueva lista invertida de forma segura
    return lista[::-1]