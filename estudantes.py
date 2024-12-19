from fastapi import APIRouter, Form, HTTPException, FastAPI

router = APIRouter()

# Simulação de banco de dados em memória
estudantes = []

@router.get("/")
async def list_estudantes():
    """
    Retrieve the list of estudantes.
    """
    return {
        "status": "success",
        "message": "Estudantes retrieved successfully.",
        "data": estudantes
    }

@router.get("/{estudante_id}")
async def get_estudante_by_id(estudante_id: int):
    """
    Retrieve an estudante by their ID.
    """
    for estudante in estudantes:
        if estudante["id"] == estudante_id:
            return {
                "status": "success",
                "message": "Estudante retrieved successfully.",
                "data": estudante
            }
    raise HTTPException(status_code=404, detail="Estudante not found.")

@router.post("/")
async def create_estudante(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...)
):
    """
    Add a new estudante to the list.
    """
    estudante = {
        "id": len(estudantes) + 1,  # Generate a simple ID
        "name": name,
        "email": email,
        "phone": phone
    }
    estudantes.append(estudante)
    return {
        "status": "success",
        "message": "Estudante added successfully.",
        "data": estudante
    }

@router.put("/{estudante_id}")
async def update_estudante(
    estudante_id: int,
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...)
):
    """
    Update an estudante's details by their ID.
    """
    for estudante in estudantes:
        if estudante["id"] == estudante_id:
            estudante.update({"name": name, "email": email, "phone": phone})
            return {
                "status": "success",
                "message": "Estudante updated successfully.",
                "data": estudante
            }
    raise HTTPException(status_code=404, detail="Estudante not found.")

@router.delete("/{estudante_id}")
async def delete_estudante(estudante_id: int):
    """
    Delete an estudante by their ID.
    """
    for index, estudante in enumerate(estudantes):
        if estudante["id"] == estudante_id:
            deleted_estudante = estudantes.pop(index)
            return {
                "status": "success",
                "message": "Estudante deleted successfully.",
                "data": deleted_estudante
            }
    raise HTTPException(status_code=404, detail="Estudante not found.")
