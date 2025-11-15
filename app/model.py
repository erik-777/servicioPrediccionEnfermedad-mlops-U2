def predecir_enfermedad(fiebre: float, precion: float, frecuencia: float) -> str:
    """
    Función simulada que retorna un diagnóstico según los síntomas.
    """
    score = fiebre + precion + frecuencia

    if score < 5:
        return "NO ENFERMO"
    elif 5 <= score < 10:
        return "ENFERMEDAD LEVE"
    elif 10 <= score < 15:
        return "ENFERMEDAD AGUDA"
    else:
        return "ENFERMEDAD CRÓNICA"
