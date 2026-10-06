# prueba-tecnica-tramites
tramites sv

## API (main/)

API de prueba en Python (FastAPI) con datos mockeados.

### Instalacion

```powershell
cd main
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Ejecucion

```powershell
uvicorn app:app --reload
```

### Endpoints

- `GET /health` - chequeo de salud del servicio.
- `GET /tramite/{id}` - devuelve datos mockeados de un tramite.

