#!/bin/bash

docker run --name=pg-data pgsql true
docker run -d --name=postgres --volumes-from=pg-data pgsql
sleep 4 
docker exec -it postgres su postgres -c "createuser -L yardstick"
docker exec -it postgres su postgres -c "createdb -O yardstick yardstick"
docker exec -it postgres su postgres -c "createuser -g yardstick -P demo"

docker run -it --name=demo --link postgres:postgres demobox tmux