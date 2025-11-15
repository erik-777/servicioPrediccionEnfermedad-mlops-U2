# 🩺 Predictor Médico – Simulación en Docker  

Este servicio implementa una **simulación de modelo de predicción médica** que, a partir de tres valores de síntomas ingresados por el usuario, determina el posible estado de salud del paciente.  

El modelo no realiza predicciones reales, sino que **emula la lógica de decisión** de un sistema de diagnóstico automatizado, devolviendo uno de los siguientes estados:  

- `NO ENFERMO`  
- `ENFERMEDAD LEVE`  
- `ENFERMEDAD AGUDA`  
- `ENFERMEDAD CRÓNICA`

## 🧱 Construcción de la imagen
```bash
docker build -t taler_semana1 .
```
## Ejecuion del Servicio
```bash
docker run -d -p 5001:5000 taller_semana1
```


El servicio quedará disponible en:  
👉 `http://localhost:5001`

---

## 🧪 Ejemplo de Uso  

Puede enviar una solicitud `POST` al endpoint `/predecir` con los tres valores de entrada (por ejemplo, síntomas medidos o valores clínicos simulados):  

```bash
curl -X POST -H "Content-Type: application/json"   -d '{"valor1": 3, "valor2": 4, "valor3": 6}'   http://localhost:5001/predecir
```

**Respuesta esperada:**
```json
{
  "resultado": "ENFERMEDAD AGUDA"
}
```
---

## 📁 Estructura del Proyecto  

```
Taller_Semana1/
│
├── app/
│   ├── main.py             # API Flask para exposición del modelo
│   ├── model.py            # Función de predicción simulada
│   └── requirements.txt    # Dependencias del proyecto
│
├── Dockerfile              # Configuración de la imagen Docker
└── README.md               # Documentación del proyecto
```

---

## 💡 Notas Técnicas  

- La aplicación corre sobre **Flask (Python 3.10)**.  
- El contenedor expone el **puerto 5000 interno**, mapeado al **5001 local**.  
- Puede modificarse el comportamiento del modelo editando `model.py`.  
- Para detener el contenedor en ejecución:
  ```bash
  docker ps        # Identificar el ID del contenedor
  docker stop <ID> # Detener el contenedor
  ```

---
