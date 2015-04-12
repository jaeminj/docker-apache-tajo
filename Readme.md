# Docker Apache TAJO 0.10.0 Ubuntu 14.04

[Origianl Project from sktelecom/ubuntu-14.10-hdw](https://registry.hub.docker.com/u/sktelecom/ubuntu14.10-hdw/) 
    $ cd src
    $ ./docker-image-apache-tajo.sh build


    $ sudo ./run-cluster.sh
    # creating cluster and logged on docker guest
    ...

    $ root@hnn-001-01:~# ./init-spark.sh
    $ root@hnn-001-01:~# ./test-spark.sh
    $ root@hnn-001-01:~# ./init-tajo.sh
    $ root@hnn-001-01:~# /usr/local/tajo/bin/start-tajo.sh
    $ root@hnn-001-01:~# ./test-tajo.sh
    $ root@hnn-001-01:~# ./test-python-tajo-client.sh
    $ root@hnn-001-01:~# ./test-hive.sh
    $ root@hnn-001-01:~# ./run-ipython-notebook.sh
    ...

    $ root@hnn-001-01:~# exit
    # logged out with removing clusters
