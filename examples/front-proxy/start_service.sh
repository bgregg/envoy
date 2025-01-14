#!/bin/sh
redis-server --protected-mode no &
python3 /code/set-redis-keys.py &
python3 /code/service.py &
envoy -c /etc/service-envoy.yaml --service-cluster "service${SERVICE_NAME}"
