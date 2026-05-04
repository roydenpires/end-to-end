from fastapi import FastAPI

api = FastAPI(
    title="Testing FASTAPI on Azure", 
    description="This is my API test", 
    version="1.0.0"
)

@api.get("/")
async def root() -> dict[str,str]:
    return {"message": "FastAPI is running on Azure Functions"}

@api.get("/health")
async def health() -> dict[str, str]:
    return {"status": "We're healthy!"}