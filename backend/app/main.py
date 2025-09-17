from fastapi import FastAPI
from app.routes import image_routes

app = FastAPI()

def create_app() -> FastAPI:
    app = FastAPI(
        title='Haircut API',
        description='API for Haircut Simulation Project',
        version='1.0.0'
    )

    # Registra rotas
    app.include_router(image_routes.router, prefix='/image', tags=['Images'])
    return app

app = create_app()
