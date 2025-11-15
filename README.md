# 🩺 Predictor Médico – Simulación en Docker  

Este servicio implementa una **simulación de modelo de predicción médica**, que recibe tres valores clínicos (`fiebre`, `presion`, `frecuencia_cardiaca`) y determina un posible estado de salud del paciente según reglas predefinidas.  

El sistema **no utiliza un modelo de Machine Learning real**, sino que emula la lógica de decisión de un sistema de diagnóstico automatizado, devolviendo una de las siguientes cinco categorías:

- `NO ENFERMO`  
- `ENFERMEDAD LEVE`  
- `ENFERMEDAD AGUDA`  
- `ENFERMEDAD CRÓNICA`  
- `ENFERMEDAD TERMINAL`  

Además, el servicio mantiene un registro persistente de las predicciones realizadas y permite obtener un **reporte estadístico** con la siguiente información:
- Número total de predicciones por categoría.  
- Las últimas 5 predicciones realizadas.  
- Fecha y hora de la última predicción.

---

## 🧱 Construcción de la imagen Docker

```bash
docker build -t taller_semana1 .
```

---

## 🚀 Ejecución del servicio

```bash
docker run -d -p 5001:5000 taller_semana1
```

El servicio quedará disponible en:  
👉 `http://localhost:5001`

---

## 🧪 Ejemplo de uso del modelo  

Puede enviar una solicitud `POST` al endpoint `/predecir` con los tres valores de entrada (por ejemplo, síntomas simulados):  

```bash
curl -X POST -H "Content-Type: application/json"   -d '{"fiebre": 38, "presion": 120, "frecuencia_cardiaca": 90}'   http://localhost:5001/predecir
```

**Respuesta esperada:**
```json
{
  "resultado": "ENFERMEDAD AGUDA"
}
```

---

## 📊 Obtener reporte de predicciones

El sistema genera automáticamente un archivo `predicciones.log` con todas las solicitudes realizadas.  
Para acceder al resumen estadístico, puede consultarse el endpoint `/reporte`:

```bash
curl -X GET http://localhost:5001/reporte
```

**Ejemplo de respuesta:**
```json
{
  "total_por_categoria": {
    "ENFERMEDAD AGUDA": 3,
    "ENFERMEDAD LEVE": 1
  },
  "ultimas_5_predicciones": [
    {"fecha": "2025-11-14 22:31:10", "fiebre": 38, "presion": 120, "frecuencia_cardiaca": 90, "resultado": "ENFERMEDAD AGUDA"}
  ],
  "ultima_fecha": "2025-11-14 22:31:10"
}
```

---

## 📁 Estructura del Proyecto  

```
Taller_Semana1/
│
├── app/
│   ├── __init__.py           # Indica que 'app' es un paquete Python
│   ├── main.py               # API Flask que expone los endpoints
│   ├── model.py              # Función de predicción simulada + registro
│   ├── requirements.txt      # Dependencias del proyecto
│   └── tests/
│       └── test_model.py     # Pruebas unitarias para el pipeline CI/CD
│
├── .github/
│   └── workflows/
│       └── ci_cd_pipeline.yaml  # Pipeline CI/CD con GitHub Actions
│
├── Dockerfile                # Construcción de la imagen Docker
└── README.md                 # Documentación del proyecto
```

---

## 💡 Notas Técnicas  

- Desarrollado en **Python 3.10** utilizando **Flask** como framework web.  
- La API expone dos rutas principales:
  - `POST /predecir` → recibe tres valores y devuelve la predicción.  
  - `GET /reporte` → muestra estadísticas acumuladas de predicciones.  
- El contenedor expone el **puerto 5000 interno**, mapeado al **5001 local**.  
- El archivo de registro `predicciones.log` se crea automáticamente en el contenedor.  
- Para detener el contenedor en ejecución:
  ```bash
  docker ps        # Identificar el ID del contenedor
  docker stop <ID> # Detener el contenedor
  ```
- Pipeline CI/CD automatizado con:
  - **Pruebas unitarias** (`pytest`) ejecutadas en GitHub Actions.  
  - **Comentarios automáticos** en Pull Requests.  
  - **Construcción y publicación** de imagen Docker en GitHub Packages.

