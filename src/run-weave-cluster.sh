#!/bin/bash

weave launch
#weave launch-dns 172.2.1.3/24

LINK=""
for i in {1..3}
do
    HOSTNAME=hdw-001-0$i
    HOST=${HOSTNAME}.weave.local 
    # C=$(weave run 10.2.1.1${i}/24 --name=$HOST -h $HOST -p 1001$i:22 -p 1920$i:9200 -d ubuntu-14.04/tajo:0.10.0 /root/start.sh)
#    C=$(weave run --with-dns 172.2.1.1${i}/24 --name=$HOSTNAME -h $HOST --net="none" -d ubuntu-14.04/tajo:0.10.0 /root/start.sh)
    C=$(weave run 172.2.1.1${i}/24 --name=$HOSTNAME -h $HOSTNAME --net="none" -d ubuntu-14.04/tajo:0.10.0 /root/start.sh)
    echo $C
done
# C=$(weave run /24 -it -h a118.jaeminj.local --net="none"  ubuntu)


HOSTNAME=hnn-001-01
HOST=${HOSTNAME}.weave.local 
#PORT="-p 8088:8088 -p 8888:8888 -p 10000:10000 -p 10010:22 -p 26002:26002 -p 26080:26080 -p 50070:50070"
mkdir -p /mnt/docker-share
#C=$(weave run 10.2.1.1/24 --name=$HOST -h $HOST $PORT -it -v /mnt/docker-share:/mnt  ubuntu-14.04/tajo:0.10.0 /root/init-nn.sh)
#C=$(weave run --with-dns 172.2.1.1/24 --name=$HOSTNAME -h $HOST --net="none" -it -v /mnt/docker-share:/mnt  ubuntu-14.04/tajo:0.10.0 /bin/bash )
C=$(weave run  172.2.1.1/24 --name=$HOSTNAME -h $HOSTNAME --net="none" -itd -v /mnt/docker-share:/mnt  ubuntu-14.04/tajo:0.10.0 /root/init-nn.sh )
docker attach $C
docker rm -f $HOSTNAME

for i in {1..3}
do
    docker rm -f hdw-001-0$i
done

#weave stop-dns
weave stop
