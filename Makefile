first-run-frontend:
	cd frontend
	npm install
	npm run start

first-run-backend:
	python3 utilities/generate-env.py
	cd backend/src
	make run-docker-debug