# Realtime-API-Monitoring

Realtime monitoring using Python (Django) & Golang as programming languages, Postgresql & Influxdb as databases, Grafana and Docker. 
This project is under development.

## Docker Containers
First, run Postgresql container on port 5434 and credentails (DB Name, USER, Password) to store API request details. <br>
    
```bash
docker run --name postgresql -d \
    -p 5434:5432 \
    --env 'DB_NAME=YOUR_POSTGRES_NAME' \
    --env 'DB_USER=YOUR_POSTGRES_USER' --env 'DB_PASS=YOUR_POSTGRES_PASSWORD' \
    --env 'DB_EXTENSION=pg_trgm' \
    --volume /srv/docker/postgres/api:/var/lib/postgresql_api \
    postgres:latest
```
