#!/bin/bash
PORT=${SERVICE_PORT:-8000}
uvicorn --host 0.0.0.0 --port ${SERVICE_PORT} server:get_app