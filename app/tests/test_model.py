import os
import json
from app.model import predecir_enfermedad, obtener_reporte, LOG_FILE

def setup_module(module):
    """Limpia archivo de log antes de comenzar."""
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

def test_prediccion_basica():
    resultado = predecir_enfermedad(38, 120, 90)
    assert resultado in [
        "NO ENFERMO", "ENFERMEDAD LEVE", "ENFERMEDAD AGUDA",
        "ENFERMEDAD CRÓNICA", "ENFERMEDAD TERMINAL"
    ]

def test_reporte_actualizado():
    predecir_enfermedad(40, 180, 130)
    reporte = obtener_reporte()
    assert "total_por_categoria" in reporte
    assert len(reporte["total_por_categoria"]) >= 1
