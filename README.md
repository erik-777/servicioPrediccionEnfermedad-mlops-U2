# 🩺 MLOps Pipeline Design -> Predictor Médico  -> V1.0.1  



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

## 1. Supuestos Generales

### Sobre el usuario (médico)

* Puede ejecutar el servicio localmente usando Docker, conforme a tu implementación actual.

* También puede consumir una API REST si la versión final se despliega en la nube.

* No necesita habilidades técnicas avanzadas.

### Sobre los datos

* Valores clínicos tabulares:
fiebre, presion, frecuencia_cardiaca.

* Para efectos del proyecto, el modelo es simulado, pero el pipeline se diseña como si fuese un ML real.

* Enfermedades comunes y huérfanas deberán manejar distinto volumen de datos.

### Sobre privacidad

Los datos procesados deben ser anonimizados.

No se almacenan datos sensibles en BD → únicamente logs locales JSONL (predicciones.log).

### Sobre la infraestructura

* El pipeline permite ejecución:

  * Local (Docker + Flask)

  * Cloud (API gateway + Docker + servidor REST)

  * Desarrollo continuo via CI/CD

## 2. Pipeline de MLOps

A continuación se describe el proceso completo end-to-end.

### Ingesta de Datos

* La ingesta proviene de registros que el médico ingresa manualmente mediante una solicitud HTTP.

* En un entorno real, vendrían de EHR, HL7, FHIR o CSV clínicos.


### Validacion y Calidad de Los Datos.

* La API debe validar:

  * Tipos numéricos

  * Rango fisiológico aceptable

### Almacenamiento y Versionamiento de los Datos.

Actualmente:

* Se registra cada predicción en predicciones.log en formato JSONL

En PROD, se recomienda:

* Data Lake → MinIO o S3

* Versionado → DVC

### Feature Engineering.

Actualmente: Se Simula la cosntruccion de los puntajes.

En PROD, se recomienda:

* Imputación de faltantes

* Normalización

* Selección de features

* Feature Store: Feast

### Entrenamiento del Modelo.

### Validacion del Modelo.

Para evaluar:

* Accuracy

* F1

* ROC-AUC

* PR-AUC (huérfanas)

Actualmente:

* Las pruebas unitarias validan que el modelo responda a las solicitudes Http, de froma correcta.

### Registro del Modelo.

Se deberia usar:

* MLflow Model Registry

* Control de versiones

* Promoción de modelos a producción

### CI/CD Testing.
 - **Pruebas unitarias** (`pytest`) ejecutadas en GitHub Actions.  

  - **Comentarios automáticos** en Pull Requests. 

### Empaquetado y Despliegue.

Despliegue local vía Dockerfile (archivo actualizado):

* Flask

* Puerto 5000 → Mapeado a 5001

Propuesta extendida:

* AWS ECS, Azure Container Apps o GCP Cloud Run

* API REST Flask/FastAPI 

### Monitoreo en Produccion.

Se recomienda:

* EvidentlyAI → Data drift

* Prometheus + Grafana → Métricas de API

* Loki → Logs centralizados

### Reentrenamiento Automatizado.

Cuando:

* Se Detecte Drift detectado

* Nuevo dataset cargado

* Validación médica

Tecnología recomendada:

* Airflow


## 3. Diseño del  Pipeline

![This is an alt text.](/imgs/DIseñoMlOPS.drawio.png "This is a sample image.")



## 4. Stack Tecnologico

| Etapa        | Tecnología                        | Justificación                      |
| ------------ | --------------------------------- | ---------------------------------- |
| API          | Flask                             | Ligero, simple, ya implementado    |
| Lógica       | Python 3.10                       | Base del proyecto                  |
| Modelo       | Reglas simuladas (actual)         | Requerido en entregable            |
| Logging      | JSONL local                       | Cumple requerimiento /reporte      |
| Testing      | Pytest                            | Integrado en tu código             |
| CI/CD        | GitHub Actions                    | Pipeline reproducible              |
| Contenedores | Docker                            | Permite ejecución local y en cloud |
| Monitoreo    | (Propuesto) Prometheus, Evidently | Requisito de MLOps                 |
| Orquestación | (Propuesto) Airflow               | Para retraining futuro             |


## 5. Changelog

| Componente    | Semana 1            | Versión Final (actual, tus archivos)                               |
| ------------- | ------------------- | ------------------------------------------------------------------ |
| Predicción    | Función simple      | Función con cálculo escalar y 5 niveles de enfermedad              |
| Logging       | No existía          | Archivo JSONL `predicciones.log` generado automáticamente          |
| Endpoints     | Sólo `/predecir`    | Ahora `/` y `/reporte` incluidos                                   |
| CI/CD         | No existía          | Pipeline integrado de pruebas (Github Actions declarado en README) |
| Testing       | No existía          | `tests/test_model.py` creado con dos pruebas unitarias reales      |
| Documentación | README básico       | README completo con endpoints y logs                               |
| Arquitectura  | Sin pipeline formal | Pipeline MLOps completo incorporado                                |
| Despliegue    | Docker simple       | Docker + API + preparación para cloud                              |
| Monitoreo     | No existía          | Propuesto: Prometheus + EvidentlyAI                                |
| Ingeniería    | Nivel básico        | Redacción profesional alineada a MLOps                             |



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

