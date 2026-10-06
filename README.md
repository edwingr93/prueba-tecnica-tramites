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

## Publicar imagen con GitHub Actions

El workflow `.github/workflows/gar-push.yml` construye `main/Dockerfile` y
publica una etiqueta inmutable con el SHA del commit en Artifact Registry.
No publica `latest` ni despliega a Cloud Run.

En GitHub, configura estas variables en **Settings > Secrets and variables >
Actions > Variables**:

- `GCP_PROJECT_ID`: `pd-ed-gar-2026`
- `GCP_REGION`: `us-central1`
- `GAR_REPOSITORY`: `tramites`

Configura estos secrets en la pestaña **Secrets**:

- `GCP_WORKLOAD_IDENTITY_PROVIDER`: output Terraform `github_workload_identity_provider`
- `GCP_SERVICE_ACCOUNT`: output Terraform `github_service_account`

Después de fusionar el workflow a `main`, cualquier push que cambie `main/` o
el propio workflow lo ejecutará. También puedes iniciarlo desde **Actions >
Build and push to Artifact Registry > Run workflow** y seleccionar la rama.
El enlace de la imagen publicada aparece en el resumen de la ejecución:

```text
us-central1-docker.pkg.dev/pd-ed-gar-2026/tramites/tramites-api:<commit-sha>
```
