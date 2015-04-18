from fabric.api import env,run

env.user='root'
env.password=''
env.roledefs = {
        'worker':[],
        'namenode':[]
        }

ip_addr_planning = 
def get_ip_addr_planning():
    if role -eq 'worker' :

    else if  role -eq 'namenode':
    
    

@hosts('worker', 'namenode')
def common_install():
    """
    wget -qO- https://get.docker.com/ | sh
    sudo usermod -aG docker ubuntu
    weave overlay network install

    sudo wget -O /usr/local/bin/weave \
              https://raw.githubusercontent.com/zettio/weave/master/weaver/weave
              sudo chmod a+x /usr/local/bin/weave

    apt-get install ethtool conntrack

    git clone https://github.com/jaeminj/docker-apache-tajo.git
    cd docker-apache-tajo/src ; 
    ./docker-image-apache-tajo.sh build
    """

@hosts('workers')
def start_worker():
    """
    export WEAVE_PASSWORD=votmdnjem
    weave launch 
    C=$(weave run 10.2.1.10/24 --name=tajow01 -h $HOST -d ubuntu-14.04/tajo:0.10.0 /root/start.sh 
    """


@namenode('namenode')
def start_namenode():
    """
    export WEAVE_PASSWORD=votmdnjem
    weave launch
    C=$(weave run 10.2.1.1/24 --name=tajo -h $HOST -d ubuntu-14.04/tajo:0.10.0 /root/init-nn.sh )
    """

@namenode('namenode')
def check_tajo():
    """
    docker attach $C
    ping 10.2.1.10
    ping 10.2.1.20
    ping 10.2.1.30
    ./init-spark.sh
    ./test-spark.sh
    ./init-tajo.sh
    /usr/local/tajo/bin/start-tajo.sh
    ./test-tajo.sh
    ./test-python-tajo-client.sh
    ./test-hive.sh
    ./run-ipython-notebook.sh
    exit
    """


def build_apache_tajo_farm():
    if len(env.hosts) < 1 :
        local("echo none hosts")
    common_install()
    start_workers()
    start_namenode()
    check_tajo()

