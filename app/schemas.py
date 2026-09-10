from typing import Literal
from pydantic import BaseModel, Field


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

PLANTAS = Literal[
    "-2",
    "-1",
    "BAJO",
    "ENTREPLANTA",
    "1ª",
    "2ª",
    "3ª",
    "4ª",
    "5ª",
    "6ª",
    "7ª",
    "8ª",
    "9ª",
    "10ª",
    "11ª",
    "12ª",
    "13ª",
    "14ª",
    "15ª",
    "NO_APLICA",
    "DESCONOCIDO",
]


class Vivienda(BaseModel):
    """DATOS DE ENTRADA."""

    metros: float = Field(gt=0, description="Superficie en metros cuadrados")
    habitaciones: int = Field(ge=0, description="Número de habitaciones")
    banos: int = Field(ge=0, description="Número de baños")
    zona: str = Field(description="Zona de Madrid")
    barrio: str = Field(description="Barrio")
    tipo_inmueble: str = Field(description="Tipo de inmueble")
    planta: str = Field(description="Planta de la vivienda")
    ascensor: Literal["S", "N", "NO_APLICA", "DESCONOCIDO"]
    localizacion: Literal["EXTERIOR", "INTERIOR", "NO_APLICA", "DESCONOCIDO"]

    terraza: bool = False
    garaje: bool = False
    jardin: bool = False
    amueblada: bool = False
    reformado: bool = False

    flag_rebaja: Literal[0,1]
    flag_loft: Literal[0,1]
    flag_nuda_propiedad: Literal[0,1]
    flag_proindiviso: Literal[0,1]
    flag_subasta: Literal[0,1]
    flag_okupada: Literal[0,1]
    flag_alquilada: Literal[0,1]
    tag_piso: Literal[0,1]
    tag_vivienda: Literal[0,1]
    tag_exterior: Literal[0,1]
    tag_metro: Literal[0,1]
    tag_amplio: Literal[0,1]
    tag_terraza: Literal[0,1]
    tag_reformado: Literal[0,1]
    tag_oportunidad: Literal[0,1]
    tag_exclusiva: Literal[0,1]
    tag_luminoso: Literal[0,1]
    tag_hogar: Literal[0,1]
    tag_espectacular: Literal[0,1]
    tag_inmobiliaria: Literal[0,1]
    tag_ático: Literal[0,1]
    tag_finca: Literal[0,1]
    tag_lujo: Literal[0,1]
    tag_vistas: Literal[0,1]
    tag_nuevo: Literal[0,1]
    tag_exclusivo: Literal[0,1]
    tag_reformada: Literal[0,1]
    tag_equipada: Literal[0,1]
    tag_casa: Literal[0,1]
    tag_parque: Literal[0,1]
    tag_garaje: Literal[0,1]
    tag_interior: Literal[0,1]
    tag_estrenar: Literal[0,1]
    tag_piscina: Literal[0,1]
    tag_funcional: Literal[0,1]
    tag_hall: Literal[0,1]
    tag_moderno: Literal[0,1]
    tag_apartamento: Literal[0,1]
    tag_suite: Literal[0,1]
    tag_prestigioso: Literal[0,1]
    tag_elegante: Literal[0,1]
    tag_impresionante: Literal[0,1]
    tag_estudio: Literal[0,1]
    tag_amueblada: Literal[0,1]
    tag_urbanización: Literal[0,1]
    tag_calefacción: Literal[0,1]
    tag_armarios: Literal[0,1]
    tag_reformar: Literal[0,1]
    tag_patio: Literal[0,1]
    tag_jardín: Literal[0,1]
    tag_chalet: Literal[0,1]
    tag_balcones: Literal[0,1]
    tag_dúplex: Literal[0,1]
    tag_portero: Literal[0,1]
    tag_electrodomésticos: Literal[0,1]
    tag_goya: Literal[0,1]
    tag_solo_particulares: Literal[0,1]
    tag_ventanales: Literal[0,1]
    tag_parcela: Literal[0,1]
    tag_abstenerse_agencias: Literal[0,1]
    tag_seguridad: Literal[0,1]


class Prediccion(BaseModel):
    """Respuesta que devuelve el endpoint de predicción."""

    precio_estimado: float
    moneda: str = "EUR"