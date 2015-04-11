#!/bin/bash

# Original URL : https://raw.githubusercontent.com/dongjoon-hyun/dockerfiles/master/ubuntu14.10-hdw/run-cluster.sh
IMG_TAG=ubuntu-14.04/tajo:0.10.0
build()
{
  sudo docker build --tag ${IMG_TAG} .
}
rmi()
{
    sudo docker rmi ${IMG_TAG}
}

case $1 in
    build)
        build
    ;;
    remove)
        rmi
    ;;
    *)
        build
    ;;
esac
