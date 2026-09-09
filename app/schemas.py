from typing import Literal

from pydantic import BaseModel, Field

# Las tres listas siguientes se generaron desde el dataset de entrenamiento.
# Si se reentrena el modelo con datos nuevos, hay que regenerarlas con:
#     for valor in sorted(df["barrio"].unique()):
#         print('    "' + valor + '",')

ZONAS = Literal[
    "arganzuela",
    "barajas",
    "barrio-de-salamanca",
    "carabanchel",
    "centro",
    "chamartin",
    "chamberi",
    "ciudad-lineal",
    "fuencarral",
    "hortaleza",
    "latina",
    "moncloa",
    "moratalaz",
    "puente-de-vallecas",
    "retiro",
    "san-blas",
    "tetuan",
    "usera",
    "vicalvaro",
    "villa-de-vallecas",
    "villaverde",
]

TIPOS_INMUEBLE = Literal[
    "Piso",
    "Ático",
    "Dúplex",
    "Estudio",
    "Casa o chalet independiente",
    "Chalet adosado",
    "Chalet pareado",
    "Chalet",
    "Casa rural",
]

BARRIOS = Literal[
    "12 de Octubre-Orcasur",
    "Abrantes",
    "Acacias",
    "Adelfas",
    "Aeropuerto",
    "Alameda de Osuna",
    "Almagro",
    "Almendrales",
    "Aluche",
    "Ambroz",
    "Amposta",
    "Apóstol Santiago",
    "Arapiles",
    "Aravaca",
    "Arcos",
    "Argüelles",
    "Arroyo del Fresno",
    "Atalaya",
    "Bellas Vistas",
    "Bernabéu-Hispanoamérica",
    "Berruguete",
    "Buena Vista",
    "Butarque",
    "Campamento",
    "Campo de las Naciones-Corralejos",
    "Canillas",
    "Canillejas",
    "Casa de Campo",
    "Casco Histórico de Barajas",
    "Casco Histórico de Vallecas",
    "Casco Histórico de Vicálvaro",
    "Castellana",
    "Castilla",
    "Chopera",
    "Chueca-Justicia",
    "Ciudad Jardín",
    "Ciudad Universitaria",
    "Colina",
    "Comillas",
    "Concepción",
    "Conde Orgaz-Piovera",
    "Costillares",
    "Cuatro Caminos",
    "Cuatro Vientos",
    "Cuzco-Castillejos",
    "Delicias",
    "El Cañaveral",
    "El Pardo",
    "El Plantío",
    "El Viso",
    "Ensanche de Vallecas - La Gavia",
    "Entrevías",
    "Estrella",
    "Fontarrón",
    "Fuente del Berro",
    "Fuentelarreina",
    "Gaztambide",
    "Goya",
    "Guindalera",
    "Hellín",
    "Horcajo",
    "Huertas-Cortes",
    "Ibiza",
    "Imperial",
    "Jerónimos",
    "La Paz",
    "Las Tablas",
    "Lavapiés-Embajadores",
    "Legazpi",
    "Lista",
    "Los Ahijones",
    "Los Berrocales",
    "Los Cerros",
    "Los Cármenes",
    "Los Rosales",
    "Los Ángeles",
    "Lucero",
    "Malasaña-Universidad",
    "Marroquina",
    "Media Legua",
    "Mirasierra",
    "Montecarmelo",
    "Moscardó",
    "Niño Jesús",
    "Nueva España",
    "Nuevos Ministerios-Ríos Rosas",
    "Numancia",
    "Opañel",
    "Orcasitas",
    "Pacífico",
    "Palacio",
    "Palomas",
    "Palomeras Bajas",
    "Palomeras sureste",
    "Palos de la Frontera",
    "Pau de Carabanchel",
    "Pavones",
    "Peñagrande",
    "Pilar",
    "Pinar del Rey",
    "Portazgo",
    "Pradolongo",
    "Prosperidad",
    "Pueblo Nuevo",
    "Puerta Bonita",
    "Puerta del Ángel",
    "Quintana",
    "Recoletos",
    "Rejas",
    "Rosas",
    "Salvador",
    "San Cristóbal",
    "San Diego",
    "San Fermín",
    "San Isidro",
    "San Juan Bautista",
    "San Pascual",
    "Sanchinarro",
    "Santa Eugenia",
    "Simancas",
    "Sol",
    "Timón",
    "Trafalgar",
    "Tres Olivos - Valverde",
    "Valdeacederas",
    "Valdebebas - Valdefuentes",
    "Valdebernardo - Valderrivas",
    "Valdecarros",
    "Valdemarín",
    "Valdezarza",
    "Vallehermoso",
    "Ventas",
    "Ventilla-Almenara",
    "Villaverde Alto",
    "Vinateros",
    "Virgen del Cortijo - Manoteras",
    "Vista Alegre",
    "Zofío",
    "Águilas",
]


class Vivienda(BaseModel):
    """DATOS DE ENTRADA."""

    metros: float = Field(gt=0, description="Superficie en metros cuadrados")
    habitaciones: int = Field(ge=0, description="Número de habitaciones")
    banos: int = Field(ge=0, description="Número de baños")
    zona: str = Field(description="Zona de Madrid")
    barrio: str = Field(description="Barrio")
    tipo_inmueble: str = Field(description="Tipo de inmueble")
    planta: str = Field(description="Planta: un número o BAJO / ENTREPLANTA")
    ascensor: Literal["S", "N", "NO_APLICA", "DESCONOCIDO"]
    localizacion: Literal["EXTERIOR", "INTERIOR", "NO_APLICA", "DESCONOCIDO"]

    # Características opcionales del anuncio para completar y ser más preciso con los tags
    terraza: bool = False
    garaje: bool = False
    jardin: bool = False
    amueblada: bool = False
    reformado: bool = False


class Prediccion(BaseModel):
    """Respuesta que devuelve el endpoint de predicción."""

    precio_estimado: float
    moneda: str = "EUR"