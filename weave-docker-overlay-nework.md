## Docker install

    wget -qO- https://get.docker.com/ | sh
    sudo usermod -aG docker ubuntu

## weave overlay network install

    sudo wget -O /usr/local/bin/weave \
              https://raw.githubusercontent.com/zettio/weave/master/weaver/weave
              sudo chmod a+x /usr/local/bin/weave
    
    apt-get install ethtool conntrack

## host1 :: launch weave and run a docker container with weave


    host1 # export WEAVE_PASSWORD=votmdnjem
    host1 # weave launch 
    host1 # C=$(weave run 10.2.1.1/24 -t -i ubuntu)



## host2 :: launch weave and run a docker container with weave

    host2 # export WEAVE_PASSWORD=votmdnjem
    host2 # weave launch
    host2 # C=$(weave run 10.2.1.2/24 -t -i ubuntu)

## host1 :: login host 1 and check the network alive.

    host1 # docker attach $C
    host1 # ping -c -q 10.2.1.2

## host1 :: login host 2 and check the network alive.

    host2 # docker attach $C
    host2 # ping -c -q 10.2.1.2

