from datetime import datetime
import json
import os

LOG_FILE = "predicciones.log"

def predecir_enfermedad(fiebre: float, presion: float, frecuencia_cardiaca: float) -> str:
    """
    Simulación de modelo médico.
    Parámetros:
      fiebre: temperatura corporal en °C
      presion: presión arterial sistólica (mmHg)
      frecuencia_cardiaca: ritmo cardiaco (latidos por minuto)
    """
    score = fiebre + (presion / 10) + (frecuencia_cardiaca / 20)

    if score < 15:
        resultado = "NO ENFERMO"
    elif 15 <= score < 20:
        resultado = "ENFERMEDAD LEVE"
    elif 20 <= score < 25:
        resultado = "ENFERMEDAD AGUDA"
    elif 25 <= score < 30:
        resultado = "ENFERMEDAD CRÓNICA"
    else:
        resultado = "ENFERMEDAD TERMINAL"

    registrar_prediccion({
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "fiebre": fiebre,
        "presion": presion,
        "frecuencia_cardiaca": frecuencia_cardiaca,
        "resultado": resultado
    })

    return resultado


def registrar_prediccion(prediccion: dict):
    """Guarda cada predicción en un archivo JSONL."""
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(prediccion) + "\n")


def obtener_reporte() -> dict:
    """Genera un resumen con estadísticas de las predicciones realizadas."""
    if not os.path.exists(LOG_FILE):
        return {
            "total_por_categoria": {},
            "ultimas_5_predicciones": [],
            "ultima_fecha": None
        }

    with open(LOG_FILE, "r") as f:
        lineas = [json.loads(l) for l in f.readlines()]

    total_por_categoria = {}
    for p in lineas:
        total_por_categoria[p["resultado"]] = total_por_categoria.get(p["resultado"], 0) + 1

    ultimas_5 = lineas[-5:]
    ultima_fecha = lineas[-1]["fecha"] if lineas else None

    return {
        "total_por_categoria": total_por_categoria,
        "ultimas_5_predicciones": ultimas_5,
        "ultima_fecha": ultima_fecha
    }
