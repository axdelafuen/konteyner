# TP2

### Architecture & Network

**1. and 2.** I initialized a Git repository, retrieved the microservices sources, and pushed them to GitLab.

`git init && git add . && git commit -m "Init" && git push`

**3.** I created a dedicated bridge network so the containers could communicate with each other using their names via internal DNS.

`docker network create food-network`

**4a.** I started the MongoDB database on this network using the official image, attaching a named volume to ensure data persistence.

`docker run -d --name mongodb --network food-network -v mongo-data:/data/db mongo`

### Microservices Build & Run

**4b. (Build)** I wrote the Dockerfiles for each service, installing dependencies before copying the source code to optimize the cache, and built their images.

`docker build -t ingredients-api ./ingredients`

**4b. (Run)** I started the containers in the required order, passing the appropriate environment variables and ports.

`docker run -d --name ingredients --network food-network ingredients-api`

`docker run -d --name calories --network food-network -e MONGODB_CONNECTION_STRING="mongodb://mongodb:27017/calories" -e MONGODB_COLLECTION="calories_data" calories-api`

`docker run -d --name recipes --network food-network -e INGREDIENTS_API_URL="http://ingredients:80" recipes-api 8081`

`docker run -d --name website --network food-network -p 8080:8080 -e RECIPE_MICROSERVICE_URL="http://recipes:8081" -e NUTRITION_MICROSERVICE_URL="http://calories:80" website-api 8080`

**5.** I verified the overall functionality of the applications to confirm the microservices were displaying correctly on the main site.

`curl http://localhost:8080`

---
Would you like me to format the actual code for the Dockerfiles in a similar copy-paste-friendly way?