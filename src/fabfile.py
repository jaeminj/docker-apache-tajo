#from fabric.api import env,run,prompt
from fabric.api import *

env.user='root'
env.password=prompt('common ', env.user, ' password:')
env.roledefs = {
        'worker':['115.68.184.118'],
        'namenode':['115.68.184.135']
        }

@roles('worker')
def test():
    run("ifconfig |grep 115")
    print env.host_string
    print str
    print i

@roles('namenode')
def put_hosts():
    hostfile_txt = """
127.0.0.1   localhost
172.2.1.1   hnn-001-01
"""
    for i  in range(0, len(env.roledefs['worker'])):
        hostfile_txtline="hdw-001-0%d 172.2.1.1%d\n" %(i, i)
        hostfile_txt += hostfile_txtline
    
    f = open("./hosts.fab", 'w')
    f.write(hostfile_txt)
    f.close()
    local("cat ./hosts.fab")
    run("ls /root/docker-apache-tajo/src")
    put("./hosts.fab", "/root/docker-apache-tajo/src/hosts")


@roles('worker', 'namenode')
def reset():
    run("weave stop")
    run("docker ps | awk '{print $1}' |  grep -v CON | while read cid ; do docker rm -f $cid ; done ") 


# @roles('worker', 'namenode')
@roles('namenode')
def common_install():
    run(" wget -qO- https://get.docker.com/ | sh ")
    run(" wget -O /usr/local/bin/weave \
        https://github.com/weaveworks/weave/releases/download/latest_release/weave")
    run("chmod a+x /usr/local/bin/weave")
    run(" apt-get -qy install ethtool conntrack git")
    run(" rm -rf docker-apache-tajo")
    run(" git clone https://github.com/jaeminj/docker-apache-tajo.git")
    with cd("docker-apache-tajo/src"):
        run("./docker-image-apache-tajo.sh build")
    run(" export WEAVE_PASSWORD=votmdnjem ")
    run(" weave launch ")
    


@roles('worker')
def start_worker():
    cmd = " weave connect " + env.roledefs['namenode'][0]
    run( cmd )
    i = env.roledefs['worker'].index(env.host_string)
    cmd = "export C=$( HOST=hdw-001-0%d weave run 172.2.1.1%d/24 --name=$HOST -h $HOST --net='none' -d ubuntu-14.04/tajo:0.10.0 /root/start.sh )" % ( i,  i )
    run( cmd )
    run(" echo $C ")



@roles('namenode')
def start_namenode():
    run("export  C=$( HOST=hnn-001-01 weave run  172.2.1.1/24 --name=$HOSTNAME -h $HOSTNAME --net='none' -itd -v /root/docker-apache-tajo/src:/mnt  ubuntu-14.04/tajo:0.10.0 /root/init-nn.sh ) " )


@roles('namenode')
def howto_tajo():
    print "login your host ", env.roledefs['namenode'][0] , "."
    print "execute the followings."

    print """
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
    common_install()
    push_hosts()
    start_worker()
    start_namenode()
    check_tajo()

