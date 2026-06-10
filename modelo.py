class Modelo:
    """Representa un modelo de inteligencia artificial con sus resultados."""

    def __init__(self, nombre_modelo, id_experimento, tipo, score):
        self.nombre_modelo = nombre_modelo
        self.id_experimento = id_experimento
        self.tipo = tipo
        self.score = score

    def __repr__(self):
        return (
            f"Modelo(nombre='{self.nombre_modelo}', "
            f"tipo='{self.tipo}', score={self.score})"
        )

    def __eq__(self, other):
        if not isinstance(other, Modelo):
            return False
        return (
            self.nombre_modelo == other.nombre_modelo
            and self.id_experimento == other.id_experimento
        )
