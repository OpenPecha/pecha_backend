from starlette import status
from fastapi import FastAPI

api = FastAPI(
    title="Pecha API",
    description= "This is the API documentation for Pecha application",
    root_path="/api/v1",
    openapi_url="/docs/openapi.json",
    redoc_url="/docs"
)


@api.get("/health", status_code=status.HTTP_204_NO_CONTENT)
async def get_health():
    return {'status': 'up'}