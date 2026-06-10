from modelo import Modelo


def obtener_mejor_modelo(modelos):
    """Devuelve el modelo con el score mas alto.

    Args:
        modelos: lista de objetos Modelo.

    Returns:
        El objeto Modelo con mayor score, o None si la lista esta vacia.
    """
    if not modelos:
        return None
    mejor = modelos[0]
    for modelo in modelos[1:]:
        if modelo.score > mejor.score:
            mejor = modelo
    return mejor


def calcular_score_medio(modelos):
    """Calcula el score medio de una lista de modelos.

    Args:
        modelos: lista de objetos Modelo.

    Returns:
        El score medio (float), o 0 si la lista esta vacia.
    """
    if not modelos:
        return 0
    total = sum(modelo.score for modelo in modelos)
    return total / len(modelos)


def filtrar_por_tipo(modelos, tipo):
    """Filtra los modelos segun su tipo.

    Args:
        modelos: lista de objetos Modelo.
        tipo: cadena con el tipo a filtrar (ej. 'clasificacion', 'regresion').

    Returns:
        Lista de modelos que coinciden con el tipo indicado.
    """
    return [modelo for modelo in modelos if modelo.tipo == tipo]


def ordenar_por_score(modelos, descendente=True):
    """Ordena los modelos por score.

    Args:
        modelos: lista de objetos Modelo.
        descendente: si es True ordena de mayor a menor (por defecto True).

    Returns:
        Nueva lista de modelos ordenada por score.
    """
    return sorted(modelos, key=lambda m: m.score, reverse=descendente)
