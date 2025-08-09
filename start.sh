#!/bin/sh
uvicorn app.main:app --host "$SERVER_HOST" --port "$SERVER_PORT" --workers "$UVICORN_WORKERS" --log-level "$LOG_LEVEL"
