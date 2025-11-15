def predecir_enfermedad(valor1: float, valor2: float, valor3: float) -> str:
    """
    Función simulada que retorna un diagnóstico según los síntomas.
    """
    score = valor1 + valor2 + valor3

    if score < 5:
        return "NO ENFERMO"
    elif 5 <= score < 10:
        return "ENFERMEDAD LEVE"
    elif 10 <= score < 15:
        return "ENFERMEDAD AGUDA"
    else:
        return "ENFERMEDAD CRÓNICA"
