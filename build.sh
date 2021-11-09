#!/bin/bash

volumes=(flask_logging, static_data)

for vol in ${volumes[@]}; do
    if [[ -z $vol ]]; then
        rm -rf $vol
    fi
done

sudo docker-compose -f docker-compose-debug.yml build