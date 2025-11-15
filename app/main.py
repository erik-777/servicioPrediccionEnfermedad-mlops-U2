from flask import Flask, request, jsonify
from model import predecir_enfermedad, obtener_reporte

app = Flask(__name__)

@app.route('/')
def home():
    return "<h3>Servicio de Predicción Médica</h3><p>Use los endpoints /predecir y /reporte</p>"

@app.route('/predecir', methods=['POST'])
def predecir():
    data = request.get_json()
    fiebre = data.get("fiebre")
    presion = data.get("presion")
    frecuencia = data.get("frecuencia_cardiaca")

    resultado = predecir_enfermedad(fiebre, presion, frecuencia)
    return jsonify({"resultado": resultado})

@app.route('/reporte', methods=['GET'])
def reporte():
    """Devuelve estadísticas de predicciones."""
    reporte = obtener_reporte()
    return jsonify(reporte)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
