from typing import List
from fastapi import APIRouter, Form, HTTPException, FastAPI

router = APIRouter()

# Simulação de banco de dados em memória
cursos = []

@router.get("/")
async def list_cursos():
    """
    Retrieve the list of cursos.
    """
    return {
        "status": "success",
        "message": "Cursos retrieved successfully.",
        "data": cursos
    }

@router.get("/{curso_id}")
async def get_curso_by_id(curso_id: int):
    """
    Retrieve a curso by its ID.
    """
    for curso in cursos:
        if curso["id"] == curso_id:
            return {
                "status": "success",
                "message": "Curso retrieved successfully.",
                "data": curso
            }
    raise HTTPException(status_code=404, detail="Curso not found.")

@router.post("/")
async def create_curso(
    name: str = Form(...),
    description: str = Form(...),
    duration: int = Form(...)
):
    """
    Add a new curso to the list.
    """
    curso = {
        "id": len(cursos) + 1,
        "name": name,
        "description": description,
        "duration": duration
    }
    cursos.append(curso)
    return {
        "status": "success",
        "message": "Curso added successfully.",
        "data": curso
    }

@router.put("/{curso_id}")
async def update_curso(
    curso_id: int,
    name: str = Form(...),
    description: str = Form(...),
    duration: int = Form(...)
):
    """
    Update a curso's details by its ID.
    """
    for curso in cursos:
        if curso["id"] == curso_id:
            curso.update({"name": name, "description": description, "duration": duration})
            return {
                "status": "success",
                "message": "Curso updated successfully.",
                "data": curso
            }
    raise HTTPException(status_code=404, detail="Curso not found.")

@router.delete("/{curso_id}")
async def delete_curso(curso_id: int):
    """
    Delete a curso by its ID.
    """
    for index, curso in enumerate(cursos):
        if curso["id"] == curso_id:
            deleted_curso = cursos.pop(index)
            return {
                "status": "success",
                "message": "Curso deleted successfully.",
                "data": deleted_curso
            }
    raise HTTPException(status_code=404, detail="Curso not found.")
