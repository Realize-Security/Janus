#!/bin/sh

CMD='gunicorn --bind 0.0.0.0:5000 manage:app'

if [[ -z $DEBUG_ENV ]]; then
  $CMD
else
  python -m debugpy --listen 0.0.0.0:5678 --wait-for-client --multiprocess -m $CMD
fi
# 