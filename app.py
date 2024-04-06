# Documentation: https://fastapi.tiangolo.com/tutorial/first-steps/
# To run the API type: uvicorn app:screening_app --reload

import re
import pandas as pd
from os import environ
from sqlalchemy import create_engine, Engine 
from sqlalchemy import URL
from rapidfuzzy import fuzz
from fastapi import FastAPI, Request 
from fastapi.responses import ORJSONResponse

# FastAPI app
screening_app = FastAPI()

# Helper functions
def get_consolidated_sanctions():
    # Get environment variables
    HOST = environ["DB_HOST"]
    PORT = environ["DB_PORT"]
    DB_NAME = environ["DB_NAME"]
    USER = environ["DB_USER"]
    PASS = environ["DB_PASS"]

    # Define connection
    connection_string = URL.create(
        drivername="postgresql+psycopg2",
        database=DB_NAME,
        host=HOST,
        port=PORT,
        username=USER,
        password=PASS
    )

    # Create engine object
    engine = create_engine(url=connection_string)

    # Load table from SQL
    df = pd.read_sql("SELECT * FROM ofac_cons_consolidated", con=engine)

# Routes of FastAPI
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
    df = get_consolidated_sanctions().head().fillna("-")
    response = df.to_dict(orient="records")
   
    return {
        "status": "success",
        "response": response
    }   