from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid

class Ejercicio(BaseModel):
    id: int
    nombre: str
    duracion: int  # en minutos
    descripcion: str
    material: str
    objetivo: str

class Sesion(BaseModel):
    id: int
    tipo: str  # "Técnica", "Física-Coordinativa", "Táctica-Juego"
    nombre: str
    dia: str
    duracion: int  # en minutos
    imagen: str
    ejercicios: List[Ejercicio]

class SemanaEntrenamiento(BaseModel):
    id: int
    mesociclo_id: int
    semana: int
    sesiones: List[Sesion]

class Mesociclo(BaseModel):
    id: int
    nombre: str
    mes: str
    descripcion: str
    color: str
    objetivo: str
    semanas: int

class MesocicloDetalle(BaseModel):
    mesociclo: Mesociclo
    objetivos: List[str]
    sesiones_semanales: List[SemanaEntrenamiento]

class PlanificacionCompleta(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    titulo: str
    descripcion: str
    categoria: str
    duracion_meses: int
    sesiones_por_semana: int
    duracion_sesion: int
    mesociclos: List[Mesociclo]
    material_basico: List[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None

# Modelos para requests
class MesocicloCreate(BaseModel):
    nombre: str
    mes: str
    descripcion: str
    color: str
    objetivo: str
    semanas: int

class EjercicioCreate(BaseModel):
    nombre: str
    duracion: int
    descripcion: str
    material: str
    objetivo: str

class SesionCreate(BaseModel):
    tipo: str
    nombre: str
    dia: str
    duracion: int
    imagen: str
    ejercicios: List[EjercicioCreate]