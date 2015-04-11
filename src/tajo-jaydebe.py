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
	
	else:
		print "No curs"
	conn.close()

else:
	print "No conn"
