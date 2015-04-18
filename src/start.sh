#!/bin/bash

cp /root/hosts /etc/hosts

service ssh start

while true; do sleep 1000; done
