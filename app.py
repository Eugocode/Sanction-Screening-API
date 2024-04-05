# Documentation: https://fastapi.tiangolo.com/tutorial/first-steps/
# To run the API type: uvicorn app:screening_app --reload
from fastapi import FastAPI

screening_app = FastAPI()

@screening_app.get("/")
async def root():
    return {
        "status" : "success",
        "result": {
            "App Title": "Simple Screening API",
            "Version": "0.0.1"
        }
    }

@screening_app.get("/screen")
async def screen(name:str, threshold: float = 0.7):
    return {
        "status": "success"
    }