#!/bin/bash
cd fundamentus
docker build --file Dockerfile . -t fundamentus
docker run -d --network=zabbix_default --name fundamentus -p 5000:5000 fundamentus