#!/bin/bash
uvicorn --host 0.0.0.0 --port ${SERVICE_PORT} server:main