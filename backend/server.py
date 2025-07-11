from fastapi import FastAPI, APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from typing import List

# Import models and services
from models.mesociclo import Mesociclo, MesocicloDetalle, SemanaEntrenamiento, PlanificacionCompleta
from services.football_service import FootballService

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Create the main app without a prefix
app = FastAPI(title="Football Training API", version="1.0.0")

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")

# Initialize service
football_service = FootballService(db)

# Dependency to get the football service
async def get_football_service():
    return football_service

# Health check endpoint
@api_router.get("/")
async def root():
    return {"message": "Football Training API is running"}

# Get all mesociclos
@api_router.get("/mesociclos", response_model=List[Mesociclo])
async def get_mesociclos(service: FootballService = Depends(get_football_service)):
    try:
        mesociclos = await service.get_all_mesociclos()
        return mesociclos
    except Exception as e:
        logger.error(f"Error getting mesociclos: {e}")
        raise HTTPException(status_code=500, detail="Error retrieving mesociclos")

# Get specific mesociclo
@api_router.get("/mesociclos/{mesociclo_id}", response_model=Mesociclo)
async def get_mesociclo(mesociclo_id: int, service: FootballService = Depends(get_football_service)):
    try:
        mesociclo = await service.get_mesociclo_by_id(mesociclo_id)
        if not mesociclo:
            raise HTTPException(status_code=404, detail="Mesociclo not found")
        return mesociclo
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting mesociclo {mesociclo_id}: {e}")
        raise HTTPException(status_code=500, detail="Error retrieving mesociclo")

# Get mesociclo with full details
@api_router.get("/mesociclos/{mesociclo_id}/detalle", response_model=MesocicloDetalle)
async def get_mesociclo_detalle(mesociclo_id: int, service: FootballService = Depends(get_football_service)):
    try:
        detalle = await service.get_mesociclo_detalle(mesociclo_id)
        if not detalle:
            raise HTTPException(status_code=404, detail="Mesociclo not found")
        return detalle
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting mesociclo detalle {mesociclo_id}: {e}")
        raise HTTPException(status_code=500, detail="Error retrieving mesociclo details")

# Get sesiones for a specific mesociclo
@api_router.get("/mesociclos/{mesociclo_id}/sesiones", response_model=List[SemanaEntrenamiento])
async def get_sesiones_mesociclo(mesociclo_id: int, service: FootballService = Depends(get_football_service)):
    try:
        sesiones = await service.get_sesiones_by_mesociclo(mesociclo_id)
        return sesiones
    except Exception as e:
        logger.error(f"Error getting sesiones for mesociclo {mesociclo_id}: {e}")
        raise HTTPException(status_code=500, detail="Error retrieving sesiones")

# Get complete planificacion
@api_router.get("/planificacion", response_model=PlanificacionCompleta)
async def get_planificacion(service: FootballService = Depends(get_football_service)):
    try:
        planificacion = await service.get_planificacion_completa()
        if not planificacion:
            raise HTTPException(status_code=404, detail="Planificación not found")
        return planificacion
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting planificacion: {e}")
        raise HTTPException(status_code=500, detail="Error retrieving planificación")

# Material básico endpoint
@api_router.get("/material-basico")
async def get_material_basico():
    try:
        material = [
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
        return {"material": material}
    except Exception as e:
        logger.error(f"Error getting material básico: {e}")
        raise HTTPException(status_code=500, detail="Error retrieving material básico")

# Initialize data endpoint (for setup)
@api_router.post("/init-data")
async def init_data(service: FootballService = Depends(get_football_service)):
    try:
        await service.init_data()
        return {"message": "Data initialized successfully"}
    except Exception as e:
        logger.error(f"Error initializing data: {e}")
        raise HTTPException(status_code=500, detail="Error initializing data")

# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Event handlers
@app.on_event("startup")
async def startup_event():
    logger.info("Football Training API starting up...")
    try:
        # Initialize data on startup
        await football_service.init_data()
        logger.info("Data initialization completed")
    except Exception as e:
        logger.error(f"Error during startup: {e}")

@app.on_event("shutdown")
async def shutdown_db_client():
    logger.info("Football Training API shutting down...")
    client.close()