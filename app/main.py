from flask import Flask, request, jsonify
from model import predecir_enfermedad

app = Flask(__name__)

@app.route('/')
def home():
    return "<h3>Servicio de Predicción Médica</h3><p>Use el endpoint /predecir</p>"

@app.route('/predecir', methods=['POST'])
def predecir():
    data = request.get_json()
    v1 = data.get("fiebre")
    v2 = data.get("precion")
    v3 = data.get("frecuencia")

    resultado = predecir_enfermedad(v1, v2, v3)
    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
