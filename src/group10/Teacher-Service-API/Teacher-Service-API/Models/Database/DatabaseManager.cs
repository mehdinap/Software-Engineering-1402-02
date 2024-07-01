
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
        private const string cloudDatabaseConnectionString = $"server={host};port={port};uid={user};pwd={password};database={name};";

        private const string localDatabaseConnectionString = "server=127.0.0.1;uid=root;pwd=sqlpassword;database=test-schema";
        private string _connectionString;
        public DatabaseManager()
        {    
            _connectionString = cloudDatabaseConnectionString;
        }

        public MySqlConnection GetConnection()
        {
            return new MySqlConnection(_connectionString);
        }
    }
}
