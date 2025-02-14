#!/bin/bash
PORT=${SERVICE_PORT:-8000}
echo "Starting server on port: $PORT"
uvicorn --host 0.0.0.0 --port $PORT server:get_app