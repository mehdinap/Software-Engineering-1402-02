
using MySql.Data.MySqlClient;
using System.Data.SqlClient;

namespace Teacher_Service_API.Models.Database
{
    public class DatabaseManager
    {
        private const string name = "defaultdb";
        private const string user = "avnadmin";
        private const string password = "AVNS_QXs1v9qBTveDtLIXZfW";
        private const string host = "mysql-374f4726-majidnamiiiii-e945.a.aivencloud.com";
        private const string port = "11741";
        private const string sslCa = "path/to/ca-certificate.crt"; // Path to the CA certificate
        private const string connectionString = $"server={host};port={port};uid={user};pwd={password};database={name};SslMode=Required;CertificateFile={sslCa}";

        private const string localDatabaseConnectionString = "server=127.0.0.1;uid=root;pwd=sqlpassword;database=test-schema";
        private string _connectionString;
        public DatabaseManager()
        {    
            _connectionString = connectionString;
        }

        public MySqlConnection GetConnection()
        {
            using (MySqlConnection connection = new MySqlConnection(connectionString))
            {
                try
                {
                    //checking if connection is available
                    connection.Open();
                    connection.Close();
                    return connection;
                }
                catch(AggregateException ex)
                {
                    Console.WriteLine($"connection failed : {ex.Message}");
                    return new MySqlConnection(connectionString);
                }
                catch (MySqlException ex)
                {
                    Console.WriteLine($"connection failed : {ex.Message}");
                    return new MySqlConnection(connectionString);
                }
            }
        }
    }
}
