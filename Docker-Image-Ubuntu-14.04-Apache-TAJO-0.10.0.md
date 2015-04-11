# Rebuiling the Docker Image, UBUNTU 14.04 TAJO 0.10.0 


[sktelecom/ubuntu-14.10-hdw](https://registry.hub.docker.com/u/sktelecom/ubuntu14.10-hdw/) 


Ubuntu 14.10에 Apache TAJO 0.10.0을 사용할수 있도록 Dockerfile과 사용예제가 이쁘게 정리된 사이트를 보았다. 그러나, 최신보다 중요한 것은 LTS, Ubuntu 14.04에 맞춰서 Docker 이미지를 만들어 보기로 했다.



ubuntu 14.10으로 tajo 0.10.0을 사용할 수 있도록 빌드되어 있다. Dockerfile을  Ubuntu LTS 버전인 
14.04를 기준으로 다시 build를 시도해봐았다.

    $ docker build -t ubuntu/tajo
    $ docker build -t ubuntu-14.04/tajo:0.10.0  .
    $ docker images
    ubuntu/tajo                 latest              60d8ed4548f2        51 minutes ago      1.526 GB
    ubuntu-14.04/tajo           0.10.0              60d8ed4548f2        51 minutes ago      1.526 GB



    $ docker build -t ubuntu/tajo

빌드를 시도했는데 에러가 생겼다. 에러가 생기는 부분이 있어 잡기 위해 Dockerfile을 수정을 했다. 14.04 때문 일까? 

    $ diff  Dockerfile Dockerfile.org 
    1,7c1,2
    < FROM ubuntu:14.04
    < MAINTAINER Jaemin Jang <jaemininj@gmail.com>
    < # The original Dockerfile Information
    < # MAINTAINER Dongjoon Hyun <dongjoon@apache.org>
    < # https://registry.hub.docker.com/u/sktelecom/ubuntu14.10-hdw/dockerfile/raw
    < 
    < ENV DEBIAN_FRONTEND noninteractive
    ---
    > FROM ubuntu:14.10
    > MAINTAINER Dongjoon Hyun <dongjoon@apache.org>
    10c5
    < RUN apt-get install -y git unzip openssh-server openssh-client python-software-properties software-properties-common protobuf-compiler ipython ipython-notebook python-matplotlib
    ---
    > RUN apt-get install -y git unzip openssh-server python-software-properties software-properties-common protobuf-compiler ipython ipython-notebook python-matplotlib



그리고 build된 이미지에 있는 설정 파일이 없어 에러가 생겼다. 그래서 Dockerfile에서 복사하는 파일을 찾아보았다. 그리고 그 파일을 다시 미리 빌딩된 Docker 이미지에서 뽑아내었다.

    $ grep COPY Dockerfile 
    COPY config /root/.ssh/
    COPY start.sh /root/
    COPY sync-hosts.sh /root/
    COPY elasticsearch.yml /usr/local/elasticsearch/config/
    COPY core-site.xml $HADOOP_PREFIX/etc/hadoop/
    COPY hdfs-site.xml $HADOOP_PREFIX/etc/hadoop/
    COPY mapred-site.xml $HADOOP_PREFIX/etc/hadoop/
    COPY yarn-site.xml $HADOOP_PREFIX/etc/hadoop/
    COPY init-nn.sh /root/
    COPY init-spark.sh /root/
    COPY test-spark.sh /root/
    COPY tajo-site.xml $TAJO_HOME/conf/
    COPY init-tajo.sh /root/
    COPY data.csv /root/
    COPY test-tajo.sh /root/
    COPY run-ipython-notebook.sh /root/
    COPY sample.ipynb /root/
    COPY test-hive.sh /root/
    
    $ grep COPY Dockerfile |while read cmd src dst ; do echo cp  $dst$src /mnt ; done 
    cp /root/.ssh/config /mnt
    cp /root/start.sh /mnt
    cp /root/sync-hosts.sh /mnt
    cp /usr/local/elasticsearch/config/elasticsearch.yml /mnt
    cp $HADOOP_PREFIX/etc/hadoop/core-site.xml /mnt
    cp $HADOOP_PREFIX/etc/hadoop/hdfs-site.xml /mnt
    cp $HADOOP_PREFIX/etc/hadoop/mapred-site.xml /mnt
    cp $HADOOP_PREFIX/etc/hadoop/yarn-site.xml /mnt
    cp /root/init-nn.sh /mnt
    cp /root/init-spark.sh /mnt
    cp /root/test-spark.sh /mnt
    cp $TAJO_HOME/conf/tajo-site.xml /mnt
    cp /root/init-tajo.sh /mnt
    cp /root/data.csv /mnt
    cp /root/test-tajo.sh /mnt
    cp /root/run-ipython-notebook.sh /mnt
    cp /root/sample.ipynb /mnt
    
    $ grep ENV Dockerfile |egrep  '(TAJO_HOME|HADOOP_PREFIX)'
    ENV HADOOP_PREFIX /usr/local/hadoop
    ENV PATH $PATH:$SPARK_HOME/bin:$HADOOP_PREFIX/bin
    ENV TAJO_HOME /usr/local/tajo
    ENV HADOOP_HOME $HADOOP_PREFIX

주어진 docker 실행스크립트 run-cluster.sh을  받아서 수정한뒤 호스트와 docker에 설치된 guest의 /mnt에 연결하기 위해 수정했다.

    $ sudo bash run-cluster.sh

    $ cp ~/run-cluster.sh run-cluster.sh.org
    $ diff run-cluster.sh.org run-cluster.sh
    11c11
    < docker run --name=$HOST -h $HOST $PORT $LINK -it  --rm sktelecom/ubuntu14.10-hdw /root/init-nn.sh
    ---
    > docker run --name=$HOST -h $HOST $PORT $LINK -it  -v /home/smileserv/LAB/tajo:/mnt --rm sktelecom/ubuntu14.10-hdw /root/init-nn.sh


    $ docker build -t ubuntu/tajo
    $ docker build -t ubuntu-14.04/tajo:0.10.0  .
    $ docker images
    ubuntu/tajo                 latest              60d8ed4548f2        51 minutes ago      1.526 GB
    ubuntu-14.04/tajo           0.10.0              60d8ed4548f2        51 minutes ago      1.526 GB

    
이렇게 해서 Ubuntu 14.04 / tajo 0.10.0 Docker 이미지를 만들어보았다. LTE보다 LTS를 사랑하니까,...



