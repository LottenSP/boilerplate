## Env
- configure everything from the `/deployment/example.env` (-> `/deployment/.env`)
- also u can check those variables into github for pipelines

## Docker
### Rebuild
    docker build -f deployment/Dockerfile -t boilerplate .
### Start
    docker-compose -f deployment/docker-compose.yml up

    docker-compose up
    docker-compose up -d    // background
    docker-compose logs -f  // log live display
### Stop
    docker-compose down

## Structure
core/       → Config, Logging, Security
db/         → DB Session, Base
models/     → ORM Models
schemas/    → Pydantic Models (Data Validation)
services/   → Business Logic
api/routes/ → FastAPI Routes
migrations/ → Alembic (later)

## Documentation
- Swagger UI generates Doc
- Visible in browser: /docs