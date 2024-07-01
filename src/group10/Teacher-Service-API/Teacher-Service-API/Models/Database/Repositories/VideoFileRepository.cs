using MySql.Data.MySqlClient;

namespace Teacher_Service_API.Models.Database.Repositories
{
    public class VideoFileRepository
    {
        private readonly DatabaseManager _databaseManager = new DatabaseManager();
        private const string path = "C:\\Users\\Asus\\Desktop";

        public async Task AddCourseVideoFileAsync(string courseId, string title, IFormFile file)
        {
            var fileId = Guid.NewGuid().ToString();
            var filePath = Path.Combine(path, "wwwroot", "uploads", fileId);
            using (var stream = new FileStream(filePath, FileMode.Create))
            {
                await file.CopyToAsync(stream);
            }
            var query = "Insert Into group10_videos(courseId,videoId,Title) VALUES (@courseId,@videoId,@title)";
            using (var connection = _databaseManager.GetConnection())
            {
                connection.Open();
                var command = new MySqlCommand(query, connection);
                command.Parameters.AddWithValue("@title", title);
                command.Parameters.AddWithValue("@courseId", courseId);
                command.Parameters.AddWithValue("@videoId", fileId);
                command.ExecuteNonQuery();
            }
        }

        public byte[] GetCourseVideo(string videoId)
        {
            var query = "select videoId from group10_videos where videoId = @videoId";
            using (var connection = _databaseManager.GetConnection())
            {
                connection.Open();
                var command = new MySqlCommand(query, connection);
                command.Parameters.AddWithValue("@videoId", videoId);
                using (var reader = command.ExecuteReader())
                {
                    if (reader.Read())
                    {
                        var fileId = reader.GetString("videoId");
                        var filePath = Path.Combine(path, "wwwroot", "uploads", fileId);
                        if (System.IO.File.Exists(filePath))
                        {
                            var fileBytes = System.IO.File.ReadAllBytes(filePath);
                            return fileBytes;
                        }
                    }
                }
            }
            return new byte[0];
        }

        public List<string> GetCourseVideosIds(string courseId)
        {
            var query = "select videoId from group10_videos where courseId = @courseId";
            using (var connection = _databaseManager.GetConnection())
            {
                connection.Open();
                var command = new MySqlCommand(query, connection);
                command.Parameters.AddWithValue("@courseId", courseId);
                var result = new List<string>();
                using (var reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        var id = reader.GetString("videoId");
                        result.Add(id);
                    }
                }
                return result;
            }
        }

        public bool DeleteVideo(string videoId)
        {
            if (DeleteVideoDataFromTable(videoId) & DeleteVideoFile(videoId))
            {
                return true;
            }
            return false;
        }
        public bool DeleteAllVideoFilesOfCourse(string courseId)
        {
            var result = true;
            var query = "select videoId from group10_videos where courseId = @courseId";
            using (var connection = _databaseManager.GetConnection())
            {
                connection.Open();
                var command = new MySqlCommand(query, connection);
                command.Parameters.AddWithValue("@courseId", courseId);
                using (var reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        var fileId = reader.GetString("videoId");
                        var filePath = Path.Combine(path, "wwwroot", "uploads", fileId);
                        if (!DeleteVideo(fileId))
                        {
                            result = false;
                        }
                    }
                    return result;
                }
            }
        }

        private bool DeleteVideoDataFromTable(string fileId)
        {
            var query = "delete from group10_videos where videoId = @videoId";
            using (var connection = _databaseManager.GetConnection())
            {
                connection.Open();
                var command = new MySqlCommand(query, connection);
                command.Parameters.AddWithValue("@videoId", fileId);
                return command.ExecuteNonQuery() > 0;
            }
        }

        private bool DeleteVideoFile(string fileId)
        {
            var filePath = Path.Combine(path, "wwwroot", "uploads", fileId);
            if (System.IO.File.Exists(filePath))
            {
                System.IO.File.Delete(filePath);
                return true;
            }
            return false;
        }
    }
}
