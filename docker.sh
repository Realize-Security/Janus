#!/bin/sh

function prune_docker() {
    echo ">> Removing all stopped containers"
    docker rm $(docker ps --filter status=exited -q)
    echo

    echo "Prune all volumes"
    docker volume prune -f
    echo

    echo "Prune all images"
    docker image prune -f
    echo

    echo "Prune all containers"
    docker container prune -f
    echo

}

function build() {
    sudo docker-compose -f docker-compose-$ENVIRONMENT.yml up --build
}

function restart() {
    echo "Reset Docker socket"
    sudo systemctl restart docker.socket
    echo

    echo "Reset Docker service"
    sudo systemctl restart docker.service
    echo
}


if [[ $2 ]] && [[ $2 = "--prune" ]]
then
    prune_docker
fi

if [[ $3 ]] && [[ $3 = "--reset" ]]
then
    restart
fi


declare -a validenvs=("dev" "test" "debug")

if [[ " ${validenvs[*]} " =~ " ${1} " ]]
then
    ENVIRONMENT=$1
    build
else
    echo "[!] First argument must be 'dev', 'test' or 'debug'"
    exit
fi



