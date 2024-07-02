using Microsoft.AspNetCore.StaticFiles;
using MySql.Data.MySqlClient;

namespace Teacher_Service_API.Models.Database.Repositories
{
    public class ImageFileRepository
    {        
        private readonly DatabaseManager _databaseManager = new DatabaseManager();
        private const string path = "C:\\Users\\Asus\\Desktop";
        public async Task AddCoursePosterFileAsync(string courseId, IFormFile file)
        {
            //use courseId as imageId
            var filePath = Path.Combine(path, "wwwroot", "uploads", courseId);
            using (var stream = new FileStream(filePath, FileMode.Create))
            {
                await file.CopyToAsync(stream);
            }
            var query = "Insert Into group10_images(imageId,type) VALUES (@imageId,@type)";
            using (var connection = _databaseManager.GetConnection())
            {
                connection.Open();
                var command = new MySqlCommand(query, connection);                
                command.Parameters.AddWithValue("@imageId", courseId);
                command.Parameters.AddWithValue("@type", "course-poster");
                command.ExecuteNonQuery();
            }
        }

        public byte[] GetCoursePoster(string courseId)
        {
            var query = "select imageId,type from group10_images where imageId = @courseId";
            using (var connection = _databaseManager.GetConnection())
            {
                connection.Open();
                var command = new MySqlCommand(query,connection);
                command.Parameters.AddWithValue("@courseId",courseId);
                using (var reader =  command.ExecuteReader())
                {
                    if (reader.Read())
                    {                        
                        var fileType = reader.GetString("type");
                        var filePath = Path.Combine(path, "wwwroot", "uploads", courseId);
                        if (System.IO.File.Exists(filePath) && fileType == "course-poster")
                        {
                            var fileBytes = System.IO.File.ReadAllBytes(filePath);                            
                            return fileBytes;
                        }
                    }
                }
            }
            return new byte[0];
        }

        public bool DeleteImage(string imageId)
        {            
            if (DeleteImageFile(imageId) & DeleteImageDataFromTable(imageId))
            {
                return true;
            }
            return false;
        }

        public bool DeleteCoursePosterFile(string courseId)
        {
            var query = "select imageId,type from group10_images where imageId = @courseId";
            using(var connection = _databaseManager.GetConnection()) 
            { 
                connection.Open();
                var command = new MySqlCommand(query, connection);
                command.Parameters.AddWithValue("@courseId", courseId);
                using (var reader = command.ExecuteReader())
                {
                    if (reader.Read())
                    {
                        var imageId = reader.GetString("imageId");
                        if (DeleteImage(imageId))
                        {
                            return true;
                        }
                    }
                    return false;
                }
            }
        }

        private bool DeleteImageFile(string imageId)
        {
            var filePath = Path.Combine(path, "wwwroot", "uploads", imageId);
            if (System.IO.File.Exists(filePath))
            {
                System.IO.File.Delete(filePath);
                return true;
            }
            return false;
        }

        private bool DeleteImageDataFromTable(string imageId)
        {
            var query = "delete from group10_images where imageId = @imageId";
            using (var connection = _databaseManager.GetConnection())
            {
                connection.Open();
                var command = new MySqlCommand(query, connection);
                command.Parameters.AddWithValue("@imageId", imageId);
                var result = command.ExecuteNonQuery();
                return result > 0;
            }
        }
    }
}
