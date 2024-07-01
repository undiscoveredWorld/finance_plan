FROM node:22-alpine
LABEL authors="yank"

WORKDIR /app

COPY package.json .
COPY package-lock.json .
RUN npm install

COPY . .

EXPOSE 3000

CMD