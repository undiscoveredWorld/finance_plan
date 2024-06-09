# Finance plan

App for control your expenses, incomes and assets

## Getting started

### Docker-compose

1. Clone this repository
2. Move in root of project(Folder `FinancePlan`)
3. Run `python utilities/genereate-env.py` and write environment variables
4. Run `docker-compose up`

### Makefile

> You need to install the `make` utility and `docker` to use it method

1. Clone this repository
2. Move in root of project(Folder `FinancePlan`)
3. Run `python utilities/genereate-env.py` and write environment variables
4. Move in `FinancePlan/src` directory
5. Run `make run-docker-production` or `make run-docker-debug`

Server will be available on http://localhost:8080/  
Swagger will be available on http://localhost:8080/docs

### Docker

1. Clone this repository
2. Move in root of project(Folder `FinancePlan`)
3. Run `python utilities/genereate-env.py` and write environment variables
4. Move in `FinancePlan/src` directory
5. Run `docker build -t finance_plan .`
6. Run `docker run --rm --name finance_plan_postgres --env-file docker.env -d -p 5432:5432 postgres:alpine`
7. Run

```Bash
docker run -p 8080:8080 \
    --rm \
    -v finance_plan:/data \
    --link finance_plan_postgres \
    -e POSTGRES_HOST=finance_plan_postgres \
    finance_plan
```

### FastAPI run

1. Clone this repository
2. Move in root of project(Folder `FinancePlan`)
3. Run `python utilities/genereate-env.py` and write environment variables
4. Move in `FinancePlan/src` directory
5. Run `python3 -m pip install -r requirements.txt`
6. Run `docker run --rm --name finance_plan_postgres --env-file docker.env -d -p 5432:5432 postgres:alpine`
7. Run `python3 -m uvicorn main:app --reload --port 8080 -- host 0.0.0.0`
