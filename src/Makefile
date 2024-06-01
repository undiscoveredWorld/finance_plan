run:
	docker build -t finance_plan .
	docker run -p 8080:8080 \
		--rm \
		-v finance_plan:/data \
		-e PATH_TO_DATA_FILE=/data/data.json \
		finance_plan

