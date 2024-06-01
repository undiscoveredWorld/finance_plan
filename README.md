# Finance plan
App for control your expenses, incomes and assets

## Getting started
### Makefile
> You need to install the `make` utility to use it method
1. Clone this repository
2. Move in `FinancePlan/src` directory
3. Run `make run`

Server will be available on http://localhost:8080/  
Swagger will be available on http://localhost:8080/docs

### Docker
1. Clone this repository
2. Move in `FinancePlan/src` directory
3. Run `docker build -t finance_plan .`
4. Run 
```Bash
docker run -p 8080:8080 \
    --rm \
    -v finance_plan:/data \
    -e PATH_TO_DATA_FILE=/data/data.json \
    finance_plan
```

### FastAPI run
1. Clone this repository
2. Move in `FinancePlan/src` directory
3. Run `python3 -m pip install -r requirements.txt`
4. Run `python3 -m uvicorn main:app --reload --port 8080 -- host 0.0.0.0`
