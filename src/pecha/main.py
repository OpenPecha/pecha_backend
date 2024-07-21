import uvicorn
from starlette import status
from fastapi import FastAPI, HTTPException,Response

from users import views

api = FastAPI(
    title="Pecha API",
    description="This is the API documentation for Pecha application",
    root_path="/api/v1",
    openapi_url="/docs/openapi.json",
    redoc_url="/docs"
)
api.include_router(views.user_router)



@api.get("/health", status_code=status.HTTP_204_NO_CONTENT)
async def get_health():
    return {'status': 'up'}


if __name__ == '__main__':
    uvicorn.run('main:api', host='0.0.0.0', port=8000
                )
