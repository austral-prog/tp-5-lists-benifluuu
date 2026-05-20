def count_occurrences(lista, elemento):
    """
    Cuenta cuántas veces aparece un elemento específico en la lista.
    
    Parámetros:
    lista (list): La lista donde se va a buscar.
    elemento: El valor u objeto que se desea contar.
    
    Retorna:
    int: La cantidad de veces que el elemento aparece en la lista.
    """
    # Utilizaremos el método nativo .count() de las listas en Python
    return lista.count(elemento)