from fastapi import FastAPI, File, UploadFile, HTTPException
from sqlalchemy import text

from backend.services.database import engine, test_database_connection
from backend.modules.resume import process_resume

app = FastAPI(
    title="AI Resume Analyzer",
    description="AI-powered resume analysis system",
    version="1.0.0"
)


@app.get("/api/health")
def health_check():
    database_status = test_database_connection()

    return {
        "status": "ok",
        "database": "connected" if database_status else "disconnected"
    }


@app.get("/api/database/health")
def database_health():
    connected = test_database_connection()

    return {
        "database": "connected" if connected else "disconnected"
    }


@app.get("/api/job-roles")
def get_job_roles():
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT
                    job_role_id,
                    role_name,
                    required_skills
                FROM job_roles
                ORDER BY job_role_id
            """)
        )

        roles = []

        for row in result:
            roles.append({
                "job_role_id": row.job_role_id,
                "role_name": row.role_name,
                "required_skills": row.required_skills
            })

    return roles

@app.post("/api/resumes/parse")
async def parse_resume(
    resume: UploadFile = File(...)
):
    """
    Upload a PDF or DOCX resume and extract its text.
    """

    try:
        file_content = await resume.read()

        result = process_resume(
            file_name=resume.filename,
            file_content=file_content
        )

        return result

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )