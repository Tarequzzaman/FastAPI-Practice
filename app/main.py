from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.api import router as api_router
from app.core.events import create_start_app_handler, create_stop_app_handler

ALLOWED_HOSTS = []

def get_application() -> FastAPI:
    application = FastAPI(debug=True)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.add_event_handler("startup", create_start_app_handler(application))
    application.add_event_handler("shutdown", create_stop_app_handler(application))
    application.include_router(api_router)
    return application


app = get_application()
