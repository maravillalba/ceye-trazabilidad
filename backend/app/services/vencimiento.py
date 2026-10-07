from datetime import date, timedelta


def calcular_fecha_vencimiento(fecha_esterilizacion: date, vida_util_dias: int) -> date:
    """Devuelve hasta qué fecha el material se considera estéril."""
    return fecha_esterilizacion + timedelta(days=vida_util_dias)