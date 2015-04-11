#Apache Tajo JDBC driver and Python Jadebe does not matched.

## Summary

Apache Tajo is a kind of  sql on hadoop. It has jdbc driver, so tried to test, and failed.


	$ ./TAJOJDBCClient.py
	Apr 11, 2015 5:02:21 AM org.apache.tajo.rpc.BlockingRpcClient$ClientChannelUpstreamHandler exceptionCaught
	SEVERE: RPC Exception:No route to host
Apache Tajo does not need  no user and password to login.

SQLLINE another jdbc sql tool for cli, it does not support, too.

	$ sqlline -u jdbc:tajo://172.17.0.160:26002/default  -d org.apache.tajo.jdbc.TajoDriver 


## Environment
I've made docker images for Apache tajo. and its cluster based on docker.
I've executed a batch and login the Apache tajo cluster main node, main node's directory /mnt
binded host home directory.
compiled TajoJDBCClient.java , executed, and it succeeded.
But on the python, it failed. 

I'll publish my testing case to  
http://github.com/jaeminj/docker-tajo-jdbc
it will be included.
1. Readme.md as this case report.
2. Dockerfile ( will be included testing files and environment )
3. build-cluster-docker-image.sh 
4. run-cluster.sh : if you execute , builds cluster and login. when logout , removes the cluster.

I wish it'll be helpful anybody  to check this case. Thanks.

## Testing Codes and Commands

	$ cat << 'EOF' > TajoJDBCClient.java
	import java.sql.Connection;
	import java.sql.ResultSet;
	import java.sql.Statement;
	import java.sql.DriverManager;
	
	public class TajoJDBCClient {
	
	
	  public static void main(String[] args) throws Exception {
	
	    try {
	      Class.forName("org.apache.tajo.jdbc.TajoDriver");
	    } catch (ClassNotFoundException e) {
	      // fill your handling code
	    	e.printStackTrace();
	    }
	
	
	    try {
		    Connection conn = DriverManager.getConnection("jdbc:tajo://172.17.0.185:26002/default");
		    // Connection conn = DriverManager.getConnection("jdbc:tajo://127.0.0.1:26002/default");
		    Statement stmt = null;
		    ResultSet rs = null;
		    try {
		      stmt = conn.createStatement();
		      rs = stmt.executeQuery("select * from table1");
		      while (rs.next()) {
			System.out.println(rs.getString(1) + "," + rs.getString(3));
		      }
		    } finally {
		      if (rs != null) rs.close();
		      if (stmt != null) stmt.close();
		      if (conn != null) conn.close();
		    }
	
	
	    }
		catch (Exception e){
		    e.printStackTrace();
	    }
	
	  }
	}
	
	EOF
	
	$ java TajoJDBCClient 
	1,1.1
	2,2.3
	3,3.4
	4,4.5
	5,5.6
	
	
	$ cat TajoJDBCClient.py
	#!/usr/bin/python
	import jpype 
	import jaydebeapi
	
	classpath = ('/usr/lib/jvm/java-7-oracle/jre/lib/'
	           ':/usr/local/tajo-0.10.0/share/jdbc-dist/tajo-jdbc-0.10.0.jar:.')
	jvm_path = '/usr/lib/jvm/java-7-oracle/jre/lib/amd64/server/libjvm.so'
	
	jpype.startJVM(jvm_path, '-Djava.class.path=%s' % classpath)
	jpype.java.lang.System.out.println("hello world")
	
	
	conn = jaydebeapi.connect('org.apache.tajo.jdbc.TajoDriver',
	                           ['jdbc:tajo://172.17.0.160:26002/default', 'annoymous', '' ],
	                           '/usr/local/tajo-0.10.0/share/jdbc-dist/tajo-jdbc-0.10.0.jar',)
	
	if conn:
		curs = conn.cursor()
		if curs:
			curs.execute("select * from table1")
			curs.fetchall()
		
		conn.close()
	
	# End of TAJOClient.py
	
	$ ./TAJOJDBCClient.py
	Apr 11, 2015 5:02:21 AM org.apache.tajo.rpc.BlockingRpcClient$ClientChannelUpstreamHandler exceptionCaught
	SEVERE: RPC Exception:No route to host
	Apr 11, 2015 5:02:24 AM org.apache.tajo.rpc.BlockingRpcClient$ClientChannelUpstreamHandler exceptionCaught
	SEVERE: RPC Exception:No route to host
	Apr 11, 2015 5:02:28 AM org.apache.tajo.rpc.BlockingRpcClient$ClientChannelUpstreamHandler exceptionCaught
	SEVERE: RPC Exception:No route to host
	Apr 11, 2015 5:02:30 AM org.apache.tajo.rpc.NettyClientBase$1 operationComplete
	SEVERE: Max retry count has been exceeded. attempts=3
	Apr 11, 2015 5:02:30 AM org.apache.tajo.rpc.BlockingRpcClient$ClientChannelUpstreamHandler exceptionCaught
	SEVERE: RPC Exception:No route to host
	Apr 11, 2015 5:02:34 AM org.apache.tajo.rpc.BlockingRpcClient$ClientChannelUpstreamHandler exceptionCaught
	SEVERE: RPC Exception:No route to host
	Apr 11, 2015 5:02:37 AM org.apache.tajo.rpc.BlockingRpcClient$ClientChannelUpstreamHandler exceptionCaught
	SEVERE: RPC Exception:No route to host
	Apr 11, 2015 5:02:40 AM org.apache.tajo.rpc.BlockingRpcClient$ClientChannelUpstreamHandler exceptionCaught
	SEVERE: RPC Exception:No route to host
	Apr 11, 2015 5:02:42 AM org.apache.tajo.rpc.NettyClientBase$1 operationComplete
	SEVERE: Max retry count has been exceeded. attempts=3
	Apr 11, 2015 5:02:42 AM org.apache.tajo.rpc.BlockingRpcClient$ClientChannelUpstreamHandler exceptionCaught
	SEVERE: RPC Exception:No route to host
	Apr 11, 2015 5:02:46 AM org.apache.tajo.rpc.BlockingRpcClient$ClientChannelUpstreamHandler exceptionCaught
	SEVERE: RPC Exception:No route to host
	Apr 11, 2015 5:02:49 AM org.apache.tajo.rpc.BlockingRpcClient$ClientChannelUpstreamHandler exceptionCaught
	SEVERE: RPC Exception:No route to host
	Apr 11, 2015 5:02:52 AM org.apache.tajo.rpc.BlockingRpcClient$ClientChannelUpstreamHandler exceptionCaught
	SEVERE: RPC Exception:No route to host
	Apr 11, 2015 5:02:54 AM org.apache.tajo.rpc.NettyClientBase$1 operationComplete
	SEVERE: Max retry count has been exceeded. attempts=3
	Traceback (most recent call last):
	  File "./jdbc.py", line 20, in <module>
	    curs.execute("select * from table1")
	  File "/usr/local/lib/python2.7/dist-packages/jaydebeapi/dbapi2.py", line 444, in execute
	    _handle_sql_exception(ex)
	  File "/usr/local/lib/python2.7/dist-packages/jaydebeapi/dbapi2.py", line 109, in _handle_sql_exception_jpype
	    raise Error
	jaydebeapi.dbapi2.Error
	Apr 11, 2015 5:02:54 AM org.apache.tajo.rpc.BlockingRpcClient$ClientChannelUpstreamHandler exceptionCaught
	SEVERE: RPC Exception:No route to host
	
