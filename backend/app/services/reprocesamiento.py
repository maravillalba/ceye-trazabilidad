def decidir_estado_lote(resultado: str) -> str:
    """Si el resultado es A_REPROCESAR, el lote no pasa a ESTERILIZADO."""
    if resultado == "A_REPROCESAR":
        return "EN_REPROCESAMIENTO"
    return "ESTERILIZADO"