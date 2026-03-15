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

## Documentation
Swagger UI generates Doc
Visible in browser: /docs