# Apache Tajo on the docker and weaver 

(Attention: Not Tested this scenario, some config required to fix!)

## Common Install
### Docker install

    wget -qO- https://get.docker.com/ | sh
    sudo usermod -aG docker ubuntu

### weave overlay network install
    sudo wget -O /usr/local/bin/weave \
      https://github.com/weaveworks/weave/releases/download/latest_release/weave

    sudo chmod a+x /usr/local/bin/weave
    
    apt-get install ethtool conntrack

    git clone https://github.com/jaeminj/docker-apache-tajo.git
    cd docker-apache-tajo/src ; 
    ./docker-image-apache-tajo.sh build


## host1 :: for tajo worker with weave


    host1 # export WEAVE_PASSWORD=votmdnjem
    host1 # weave launch 
    host1 # C=$(weave run 10.2.1.10/24 --name=worker1 -h $HOST -d ubuntu-14.04/tajo:0.10.0 /root/start.sh )



## host2 :: for tajo worker with weave

    host2 # export WEAVE_PASSWORD=votmdnjem
    host2 # weave launch
    host1 # C=$(weave run 10.2.1.20/24 --name=worker2 -h $HOST -d ubuntu-14.04/tajo:0.10.0 /root/start.sh )

## host3 ::  for tajo worker with weave

    
    host3 # export WEAVE_PASSWORD=votmdnjem
    host3 # weave launch
    host3 # C=$(weave run 10.2.1.30/24 --name=worker3 -h $HOST -d ubuntu-14.04/tajo:0.10.0 /root/start.sh )



## host0 :: for tajo name node with weave

    
    host0 # export WEAVE_PASSWORD=votmdnjem
    host0 # weave launch
    host0 # weave launch-dns 10.2.1.3/24
    host0 # C=$(weave run 10.2.1.1/24 --name=tajo -h hnn-001-01 -d ubuntu-14.04/tajo:0.10.0 /root/init-nn.sh )
    host0 # docker attach $C
    host0 # ping 10.2.1.10
    host0 # ping 10.2.1.20
    host0 # ping 10.2.1.30
    host0 # ./init-spark.sh
    host0 # ./test-spark.sh
    host0 # ./init-tajo.sh
    host0 # /usr/local/tajo/bin/start-tajo.sh
    host0 # ./test-tajo.sh
    host0 # ./test-python-tajo-client.sh
    host0 # ./test-hive.sh
    host0 # ./run-ipython-notebook.sh
    
    host0 # exit


# After Testing, I'll make a fabfile for building apache tajo farm on the weave.

