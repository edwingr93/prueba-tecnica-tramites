"""API de prueba para consulta de tramites.

Expone:
- GET /health: chequeo de salud del servicio.
- GET /tramite/{id}: devuelve datos mockeados de un tramite.
"""
from datetime import datetime

from fastapi import FastAPI, HTTPException

app = FastAPI(title="Tramites API", version="1.0.0")

# Datos mockeados de ejemplo para pruebas.
_TRAMITES_MOCK = {
    "1": {
        "id": "1",
        "tipo": "Certificado de residencia",
        "estado": "en_proceso",
        "solicitante": "Juan Perez",
        "fecha_creacion": "2024-01-15",
    },
    "2": {
        "id": "2",
        "tipo": "Licencia de construccion",
        "estado": "aprobado",
        "solicitante": "Maria Gomez",
        "fecha_creacion": "2024-02-10",
    },
    "3": {
        "id": "3",
        "tipo": "Permiso de funcionamiento",
        "estado": "rechazado",
        "solicitante": "Carlos Ruiz",
        "fecha_creacion": "2024-03-05",
    },
}


@app.get("/health")
def health():
    return {"status": "ok", "timestamp": datetime.utcnow().isoformat()}


@app.get("/tramite/{tramite_id}")
def get_tramite(tramite_id: str):
    tramite = _TRAMITES_MOCK.get(tramite_id)
    if tramite is None:
        # Si no existe en el mock, se devuelve un registro generico de prueba.
        return {
            "id": tramite_id,
            "tipo": "Tramite generico",
            "estado": "en_proceso",
            "solicitante": "Usuario de prueba",
            "fecha_creacion": "2024-01-01",
        }
    return tramite
