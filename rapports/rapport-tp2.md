# TP2

### Architecture & Network

**1. and 2.**

`git init && git add . && git commit -m "" && git push`

**3.** Create a dedicated bridge network so the containers could communicate with each other using their names via internal DNS.

`docker network create bridge-network`

**4a.** I started the MongoDB database on this network.

`docker run -d --name mongodb --network bridge-network -v mongo-data:/data/db mongo`

### Microservices Build & Run

**4b. (Build)** I wrote the Dockerfiles for each service, installing dependencies before copying the source code to optimize the cache, and built their images.

- `docker build -t calories-api ./calories`
- `docker build -t ingredients-api ./ingredients`
- `docker build -t recipes-api ./recipes`
- `docker build -t web-app ./website`

**4b. (Run)** I started the containers in the required order, passing the appropriate environment variables and ports.

`docker run -d --name ingredients-api --network bridge-network ingredients-api`

`docker run -d --name calories-api --network bridge-network -e MONGODB_CONNECTION_STRING="mongodb://mongodb:27017/calories-api" -e MONGODB_COLLECTION="calories_data" calories-api`

`docker run -d --name recipes-api --network bridge-network -e INGREDIENTS_API_URL="http://ingredients:80" recipes-api 8081`

`docker run -d --name web-app --network bridge-network -p 8080:8080 -e RECIPE_MICROSERVICE_URL="http://recipes:8081" -e NUTRITION_MICROSERVICE_URL="http://calories:80" web-app 8080`

**5.** Check functionality of the applications to confirm the microservices were displaying correctly on the main site.

`curl http://localhost:8080`
