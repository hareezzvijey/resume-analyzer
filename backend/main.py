from fastapi import FastAPI

from services.database import test_database_connection


app = FastAPI(
    title="AI Resume Analyzer",
    description="AI-powered resume analysis system",
    version="1.0.0"
)


@app.get("/api/health")
def health_check():
    """
    Check whether the backend and database are available.
    """

    database_status = test_database_connection()

    return {
        "status": "ok",
        "database": "connected" if database_status else "disconnected"
    }