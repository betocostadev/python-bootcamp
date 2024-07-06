# Workout API - Main
# Description: Main file for the Workout API

from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Workout API",
    description="API to manage workouts - DIO challenge",
    version="0.1.0",
)

# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info", reload=True)

# engine = create_engine(
#     f"{os.getenv('DATABASE_URL')}"
# )

print(os.getenv("DATABASE_URL"))
