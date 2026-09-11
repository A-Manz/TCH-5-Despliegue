# TCH-5-Despliegue
## Tasador de precios de vivienda en venta en Madrid

API REST de un modelo de machine learning entrenado para estimar el precio de venta de una vivienda en Madrid a partir de sus características.  
El modelo procede del [proyecto final de ML del Bootcamp](https://github.com/Gabriel-Caruso/ML-idealista) de Data Science + IA de TheBridge

### URL pública

Home: https://tch-5-despliegue.onrender.com  
Documentación interactiva: https://tch-5-despliegue.onrender.com/docs  
No requiere ninguna instalación.  

El servicio está alojado en el plan gratuito de Render. La primera petición puede demorarse al menos un minuto.  

### Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/` | Información general de la API y listado de endpoints |
| GET | `/predict` | Predicción a partir de los nueve campos obligatorios, enviados en la URL |
| POST | `/predict` | Predicción a partir del esquema completo, enviado como JSON |
| GET | `/docs` | Documentación interactiva generada automáticamente |


### Cómo usarla

#### Predicción con GET:

1. Accede al siguiente elemento:  

![GET/predict]("img/img-1.png")  

2. Click en "Try it out"

![Try]("img/img-2.png")  

3. Rellena el formulario con las características y ejecuta el programa.
4. Encuentra tu resultado aquí:

![resultado]("img/img-4.png")  


#### Predicción con POST

Se trata de una petición a través de un JSON.  
En esta petición encontrarás todas las features del modelo, incluyendo tags binarios (0, 1) para indicar la mayor cantidad de características de la vivienda.
Los siguientes campos son obligatorios:
 
| Campo | Tipo | Valores |
|---|---|---|
| `metros` | número | Mayor que cero |
| `habitaciones_limpio` | entero | Cero o más |
| `baños_limpio` | entero | Cero o más |
| `zona` | texto | 21 distritos de Madrid |
| `barrio` | texto | 139 barrios |
| `tipo_inmueble` | texto | 9 tipos |
| `planta_limpio` | texto | Número con ordinal (`3ª`), `BAJO`, `ENTREPLANTA`, `-1`, `-2`, `NO_APLICA`, `DESCONOCIDO` |
| `ascensor_limpio` | texto | `S`, `N`, `NO_APLICA`, `DESCONOCIDO` |
| `localizacion_limpio` | texto | `EXTERIOR`, `INTERIOR`, `NO_APLICA`, `DESCONOCIDO` |

## Autores
 
Ramiro Caruso y Ana Manzanares