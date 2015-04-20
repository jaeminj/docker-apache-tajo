# Apache Tajo on the docker and weaver 


* This Document has been depreated since 2015-04-18.
* This current result, you can find in src/run-weave-cluster.sh src/fabfile.py.
** src/run-weave-cluster.sh :
** src/fabfile.py  


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
    docker pull jaeminj/ubuntu-14.04-apache-tajo-0.10.0

## host${i} for workers


    host1 # export WEAVE_PASSWORD=votmdnjem
    host1 # weave launch 
    host1 # C=$(weave run 172.2.1.1${i}/24 --name=worker1 -h $HOST -d jaeminj/ubuntu-14.04-apache-tajo.0.10.0 /root/start.sh )





## host0 for namenode

    
    host0 # export WEAVE_PASSWORD=votmdnjem
    host0 # weave launch
    host0 # C=$(weave run 172.2.1.1/24 --name=tajo -h hnn-001-01 -d jaeminj/ubuntu-14.04-apache-tajo-0.10.0 /root/init-nn.sh )
    host0 # docker attach $C
    host0 # ping 172.2.1.10
    host0 # ping 172.2.1.20
    host0 # ping 172.2.1.30
    host0 # ./init-spark.sh
    host0 # ./test-spark.sh
    host0 # ./init-tajo.sh
    host0 # /usr/local/tajo/bin/start-tajo.sh
    host0 # ./test-tajo.sh
    host0 # ./test-python-tajo-client.sh
    host0 # ./test-hive.sh
    host0 # ./run-ipython-notebook.sh
    
    host0 # exit


## fabric automation support

    fab -l

    # cat build-weave-apache-tajo.sh

    fab common_install
    fab put_hosts
    fab start_worker
    fab start_namenode
    fab howto_tajo

