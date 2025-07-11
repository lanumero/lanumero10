from motor.motor_asyncio import AsyncIOMotorDatabase
from models.mesociclo import Mesociclo, SemanaEntrenamiento, MesocicloDetalle, PlanificacionCompleta
from typing import List, Optional
import logging

logger = logging.getLogger(__name__)

class FootballService:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db
        self.mesociclos_collection = db.mesociclos
        self.sesiones_collection = db.sesiones_semanales
        self.planificaciones_collection = db.planificaciones

    async def get_all_mesociclos(self) -> List[Mesociclo]:
        """Obtener todos los mesociclos"""
        try:
            cursor = self.mesociclos_collection.find({})
            mesociclos_data = await cursor.to_list(length=None)
            return [Mesociclo(**mesociclo) for mesociclo in mesociclos_data]
        except Exception as e:
            logger.error(f"Error getting mesociclos: {e}")
            return []

    async def get_mesociclo_by_id(self, mesociclo_id: int) -> Optional[Mesociclo]:
        """Obtener un mesociclo específico"""
        try:
            mesociclo_data = await self.mesociclos_collection.find_one({"id": mesociclo_id})
            if mesociclo_data:
                return Mesociclo(**mesociclo_data)
            return None
        except Exception as e:
            logger.error(f"Error getting mesociclo {mesociclo_id}: {e}")
            return None

    async def get_sesiones_by_mesociclo(self, mesociclo_id: int) -> List[SemanaEntrenamiento]:
        """Obtener sesiones de un mesociclo específico"""
        try:
            cursor = self.sesiones_collection.find({"mesociclo_id": mesociclo_id})
            sesiones_data = await cursor.to_list(length=None)
            return [SemanaEntrenamiento(**sesion) for sesion in sesiones_data]
        except Exception as e:
            logger.error(f"Error getting sesiones for mesociclo {mesociclo_id}: {e}")
            return []

    async def get_mesociclo_detalle(self, mesociclo_id: int) -> Optional[MesocicloDetalle]:
        """Obtener detalle completo de un mesociclo"""
        try:
            mesociclo = await self.get_mesociclo_by_id(mesociclo_id)
            if not mesociclo:
                return None
            
            sesiones = await self.get_sesiones_by_mesociclo(mesociclo_id)
            
            # Objetivos por mesociclo (esto podría venir de la base de datos también)
            objetivos_map = {
                1: ["Familiarización con el balón", "Coordinación básica", "Diversión y participación"],
                2: ["Técnica individual", "Pase y recepción", "Control del balón"],
                3: ["Perfeccionamiento técnico", "Coordinación avanzada", "Creatividad"],
                4: ["Juego colectivo", "Conceptos tácticos básicos", "Competencia sana"],
                5: ["Consolidación", "Aplicación práctica", "Evaluación final"]
            }
            
            objetivos = objetivos_map.get(mesociclo_id, [])
            
            return MesocicloDetalle(
                mesociclo=mesociclo,
                objetivos=objetivos,
                sesiones_semanales=sesiones
            )
        except Exception as e:
            logger.error(f"Error getting mesociclo detalle {mesociclo_id}: {e}")
            return None

    async def get_planificacion_completa(self) -> Optional[PlanificacionCompleta]:
        """Obtener la planificación completa"""
        try:
            planificacion_data = await self.planificaciones_collection.find_one({})
            if planificacion_data:
                return PlanificacionCompleta(**planificacion_data)
            return None
        except Exception as e:
            logger.error(f"Error getting planificacion completa: {e}")
            return None

    async def create_planificacion(self, planificacion: PlanificacionCompleta) -> PlanificacionCompleta:
        """Crear una nueva planificación"""
        try:
            planificacion_dict = planificacion.dict()
            await self.planificaciones_collection.insert_one(planificacion_dict)
            return planificacion
        except Exception as e:
            logger.error(f"Error creating planificacion: {e}")
            raise

    async def init_data(self):
        """Inicializar datos de ejemplo"""
        try:
            # Verificar si ya hay datos
            count = await self.mesociclos_collection.count_documents({})
            if count > 0:
                logger.info("Data already exists, skipping initialization")
                return

            # Datos de mesociclos
            mesociclos_data = [
                {
                    "id": 1,
                    "nombre": "Adaptación y Familiarización",
                    "mes": "Mes 1",
                    "descripcion": "Introducción al fútbol 7, familiarización con el balón y adaptación física básica",
                    "color": "bg-blue-500",
                    "objetivo": "Crear una base sólida para el aprendizaje futuro",
                    "semanas": 4
                },
                {
                    "id": 2,
                    "nombre": "Técnica Individual Básica",
                    "mes": "Mes 2",
                    "descripcion": "Desarrollo de habilidades técnicas fundamentales: pase, recepción, conducción",
                    "color": "bg-green-500",
                    "objetivo": "Dominar los fundamentos técnicos del fútbol",
                    "semanas": 4
                },
                {
                    "id": 3,
                    "nombre": "Técnica Individual Avanzada",
                    "mes": "Mes 3",
                    "descripcion": "Perfeccionamiento técnico y coordinación con balón",
                    "color": "bg-orange-500",
                    "objetivo": "Mejorar la técnica individual y coordinación",
                    "semanas": 4
                },
                {
                    "id": 4,
                    "nombre": "Técnica Colectiva y Táctica",
                    "mes": "Mes 4",
                    "descripcion": "Introducción a conceptos tácticos básicos y juego colectivo",
                    "color": "bg-purple-500",
                    "objetivo": "Desarrollar el juego en equipo y nociones tácticas",
                    "semanas": 4
                },
                {
                    "id": 5,
                    "nombre": "Consolidación y Juego",
                    "mes": "Mes 5",
                    "descripcion": "Consolidación de aprendizajes y aplicación en situaciones reales de juego",
                    "color": "bg-red-500",
                    "objetivo": "Aplicar todos los conocimientos adquiridos",
                    "semanas": 4
                }
            ]

            # Insertar mesociclos
            await self.mesociclos_collection.insert_many(mesociclos_data)

            # Datos de sesiones semanales (ejemplo para las primeras 2 semanas)
            sesiones_data = [
                {
                    "id": 1,
                    "mesocicloId": 1,
                    "semana": 1,
                    "sesiones": [
                        {
                            "id": 1,
                            "tipo": "Técnica",
                            "nombre": "Familiarización con el balón",
                            "dia": "Lunes",
                            "duracion": 90,
                            "imagen": "https://images.unsplash.com/photo-1574242957680-7c8371ed191e",
                            "ejercicios": [
                                {
                                    "id": 1,
                                    "nombre": "Saludo y presentación",
                                    "duracion": 10,
                                    "descripcion": "Círculo de presentación, explicación de reglas básicas",
                                    "material": "Ninguno",
                                    "objetivo": "Crear ambiente de confianza y establecer normas"
                                },
                                {
                                    "id": 2,
                                    "nombre": "Calentamiento dinámico",
                                    "duracion": 15,
                                    "descripcion": "Carrera suave, movilidad articular, estiramientos dinámicos",
                                    "material": "Conos, silbato",
                                    "objetivo": "Preparar el cuerpo para la actividad física"
                                },
                                {
                                    "id": 3,
                                    "nombre": "Toque libre con el balón",
                                    "duracion": 20,
                                    "descripcion": "Cada jugador con su balón, exploración libre de toques",
                                    "material": "1 balón por jugador",
                                    "objetivo": "Familiarización inicial con el balón"
                                },
                                {
                                    "id": 4,
                                    "nombre": "Conducción básica",
                                    "duracion": 25,
                                    "descripcion": "Conducción con ambos pies en línea recta y curvas",
                                    "material": "Balones, conos",
                                    "objetivo": "Desarrollar control básico del balón"
                                },
                                {
                                    "id": 5,
                                    "nombre": "Juego libre",
                                    "duracion": 15,
                                    "descripcion": "Partido libre 4vs4 sin reglas complejas",
                                    "material": "Balones, porterías pequeñas",
                                    "objetivo": "Aplicar lo aprendido en situación de juego"
                                },
                                {
                                    "id": 6,
                                    "nombre": "Vuelta a la calma",
                                    "duracion": 5,
                                    "descripcion": "Estiramientos suaves y reflexión del entrenamiento",
                                    "material": "Ninguno",
                                    "objetivo": "Relajación y evaluación positiva"
                                }
                            ]
                        },
                        {
                            "id": 2,
                            "tipo": "Física-Coordinativa",
                            "nombre": "Desarrollo coordinativo básico",
                            "dia": "Miércoles",
                            "duracion": 90,
                            "imagen": "https://images.unsplash.com/photo-1650897877790-0e171d2207dc",
                            "ejercicios": [
                                {
                                    "id": 1,
                                    "nombre": "Activación corporal",
                                    "duracion": 10,
                                    "descripcion": "Movimientos articulares y activación muscular",
                                    "material": "Ninguno",
                                    "objetivo": "Preparar el cuerpo para el ejercicio"
                                },
                                {
                                    "id": 2,
                                    "nombre": "Circuito coordinativo",
                                    "duracion": 25,
                                    "descripcion": "Saltos, giros, desplazamientos laterales entre conos",
                                    "material": "Conos, aros, escalera de coordinación",
                                    "objetivo": "Desarrollar coordinación general"
                                },
                                {
                                    "id": 3,
                                    "nombre": "Equilibrio y propiocepción",
                                    "duracion": 15,
                                    "descripcion": "Ejercicios de equilibrio estático y dinámico",
                                    "material": "Balones, superficies inestables",
                                    "objetivo": "Mejorar el equilibrio y propiocepción"
                                },
                                {
                                    "id": 4,
                                    "nombre": "Velocidad de reacción",
                                    "duracion": 20,
                                    "descripcion": "Juegos de reacción a estímulos visuales y auditivos",
                                    "material": "Conos de colores, silbato",
                                    "objetivo": "Desarrollar velocidad de reacción"
                                },
                                {
                                    "id": 5,
                                    "nombre": "Juego coordinativo",
                                    "duracion": 15,
                                    "descripcion": "Juegos que combinen coordinación y diversión",
                                    "material": "Balones, conos",
                                    "objetivo": "Aplicar coordinación en contexto lúdico"
                                },
                                {
                                    "id": 6,
                                    "nombre": "Relajación",
                                    "duracion": 5,
                                    "descripcion": "Respiración y relajación muscular",
                                    "material": "Ninguno",
                                    "objetivo": "Vuelta a la calma progresiva"
                                }
                            ]
                        },
                        {
                            "id": 3,
                            "tipo": "Táctica-Juego",
                            "nombre": "Introducción al juego colectivo",
                            "dia": "Viernes",
                            "duracion": 90,
                            "imagen": "https://images.unsplash.com/photo-1573639615462-3a16eabd9390",
                            "ejercicios": [
                                {
                                    "id": 1,
                                    "nombre": "Calentamiento con balón",
                                    "duracion": 15,
                                    "descripcion": "Trote suave conduciendo el balón",
                                    "material": "1 balón por jugador",
                                    "objetivo": "Activación con familiarización del balón"
                                },
                                {
                                    "id": 2,
                                    "nombre": "Pases por parejas",
                                    "duracion": 20,
                                    "descripcion": "Pases cortos estáticos, aumentando progresivamente la distancia",
                                    "material": "Balones",
                                    "objetivo": "Introducir el concepto de pase"
                                },
                                {
                                    "id": 3,
                                    "nombre": "Juego de persecución",
                                    "duracion": 15,
                                    "descripcion": "El que la pica debe tocar con el balón controlado",
                                    "material": "Balones",
                                    "objetivo": "Combinar diversión con control del balón"
                                },
                                {
                                    "id": 4,
                                    "nombre": "Partidillo 3vs3",
                                    "duracion": 25,
                                    "descripcion": "Partidos cortos con rotaciones, porterías pequeñas",
                                    "material": "Balones, porterías pequeñas, petos",
                                    "objetivo": "Aplicar conceptos básicos en situación real"
                                },
                                {
                                    "id": 5,
                                    "nombre": "Tiros a portería",
                                    "duracion": 10,
                                    "descripcion": "Tiros libres desde diferentes posiciones",
                                    "material": "Balones, porterías",
                                    "objetivo": "Desarrollar la precisión en el tiro"
                                },
                                {
                                    "id": 6,
                                    "nombre": "Charla final",
                                    "duracion": 5,
                                    "descripcion": "Comentarios positivos y despedida",
                                    "material": "Ninguno",
                                    "objetivo": "Refuerzo positivo y motivación"
                                }
                            ]
                        }
                    ]
                }
            ]

            # Insertar sesiones
            await self.sesiones_collection.insert_many(sesiones_data)

            # Crear planificación general
            planificacion = PlanificacionCompleta(
                titulo="Entrenamiento Fútbol 7 - Benjamines",
                descripcion="Planificación completa de entrenamiento para benjamines en fútbol 7",
                categoria="Benjamines (8-10 años)",
                duracion_meses=5,
                sesiones_por_semana=3,
                duracion_sesion=90,
                mesociclos=[Mesociclo(**m) for m in mesociclos_data],
                material_basico=[
                    "Balones de fútbol (nº 3 o 4)",
                    "Conos de diferentes colores",
                    "Petos o camisetas de entrenamiento",
                    "Porterías pequeñas (portátiles)",
                    "Aros de coordinación",
                    "Escalera de coordinación",
                    "Silbato",
                    "Cronómetro",
                    "Bidones de agua",
                    "Botiquín básico"
                ]
            )

            await self.planificaciones_collection.insert_one(planificacion.dict())

            logger.info("Data initialized successfully")
            
        except Exception as e:
            logger.error(f"Error initializing data: {e}")
            raise