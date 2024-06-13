build:
	docker build -t finance_plan .

postgres-docker-run:
	docker run --rm --name finance_plan_postgres --env-file docker.env -d -p 5432:5432 postgres:alpine

finance-plan-run:
	docker run -p 8080:8080 \
		--rm \
		-v finance_plan:/data \
		--link finance_plan_postgres \
		-e POSTGRES_HOST=finance_plan_postgres \
		finance_plan

adminer-run:
	docker run -p 8081:8080 \
	-d \
	--rm \
	--link finance_plan_postgres \
	adminer

run-docker-production:
	make build
	make postgres-docker-run
	sleep 3
	make finance_plan_run

run-docker-debug:
	make build
	make postgres-docker-run
	sleep 3
	make adminer-run
	make finance-plan-run
