
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
