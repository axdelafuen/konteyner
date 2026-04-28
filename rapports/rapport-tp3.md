# TP3

### Workdpress example

**1. and 2.**

`touch docker-compose.yaml`

Copy-paste from the word press template.

`docker-compose up -d`

**3.** 

`docker-compose down`

`docker-compose up -d`

Data are still there, persistency works well.

**4.** Remove all data (volumes)

`docker compose down -v`

### docker-compose for tp project

**5.** Run docker compose down (without -v). When you run docker compose up again, your MongoDB data will still be there.

**6.**  (Network Isolation):

Test that website cannot talk to mongodb directly:

```sh
docker compose exec website ping mongodb
```

**8. & 9.** Check the status of containers while they start:

```
docker compose ps
```