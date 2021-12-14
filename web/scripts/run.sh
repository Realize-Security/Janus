#!/bin/sh

if [ -z "$FLASK_DEBUG" ]; then
  python -m debugpy --listen 0.0.0.0:5678 --wait-for-client -m flask run --host=0.0.0.0
elif [ -z "$FLASK_DEV" ]; then
  python -m flask run --host=0.0.0.0
else
  gunicorn --bind 0.0.0.0:5000 manage:app
fi
