using MySql.Data.MySqlClient;
using Teacher_Service_API.Models.DTOs;

namespace Teacher_Service_API.Models.Database.Repositories
{
    public class CourseRepository
    {
        private readonly DatabaseManager _databaseManager;
        private readonly VideoFileRepository _videoRepository;
        private readonly ImageFileRepository _imageFileRepository;
        private readonly ExamRepository _examRepository;
        public CourseRepository(DatabaseManager databaseManager,VideoFileRepository videoFileRepository,ImageFileRepository imageFileRepository,ExamRepository examRepository)
        {
            _databaseManager = databaseManager;
            _videoRepository = videoFileRepository;
            _imageFileRepository = imageFileRepository;
            _examRepository = examRepository;
        }

        public string AddCourse(string teacherId, CourseDTO newCourse)
        {
            var query = "Insert Into group10_courses(TeacherId, Id, Name, Description, Objectives) VALUES (@TeacherId, @Id, @Name, @Description, @Objectives)";
            var id = Guid.NewGuid().ToString();
            using (var connection = _databaseManager.GetConnection())
            {
                connection.Open();
                var command = new MySqlCommand(query, connection);
                command.Parameters.AddWithValue("@TeacherId", teacherId);
                command.Parameters.AddWithValue("@Id", id);
                command.Parameters.AddWithValue("@Name", newCourse.Name);
                command.Parameters.AddWithValue("@Description", newCourse.Description);
                command.Parameters.AddWithValue("@Objectives", newCourse.Objectives);
                command.ExecuteNonQuery();
            }
            return id;
        }


        public List<CourseDTO> GetAllCoursesOfTeacher(string teacherId)
        {
            var query = "Select * From group10_courses Where teacherId = @teacherId";
            using (var connection = _databaseManager.GetConnection())
            {
                connection.Open();
                var command = new MySqlCommand(query, connection);
                command.Parameters.AddWithValue("@teacherId", teacherId);
                using (var reader = command.ExecuteReader())
                {
                    var result = new List<CourseDTO>();
                    while (reader.Read())
                    {
                        var id = reader.GetString("Id");
                        var name = reader.GetString("Name");
                        var description = reader.GetString("Description");
                        var objectives = reader.GetString("Objectives");
                        result.Add(new CourseDTO(id, description, name, objectives));
                    }

                    return result;
                }
            }
        }

        public CourseDTO GetCourseById(string id)
        {
            var query = "Select * From group10_courses Where Id = @id";
            using (var connection = _databaseManager.GetConnection())
            {
                connection.Open();
                var command = new MySqlCommand(query, connection);
                command.Parameters.AddWithValue("@id", id);
                using (var reader = command.ExecuteReader())
                {
                    reader.Read();
                    var name = reader.GetString("Name");
                    var description = reader.GetString("Description");
                    var objectives = reader.GetString("Objectives");
                    return new CourseDTO(id, description, name, objectives);
                }
            }
        }

        public List<VideoMetaData> GetCourseVideosMetaData(string courseId)
        {
            var result = new List<VideoMetaData>();
            var query = "Select videoId,title From group10_videos Where courseId = @courseId";
            using (var connection = _databaseManager.GetConnection())
            {
                connection.Open();
                var command = new MySqlCommand(query, connection);
                command.Parameters.AddWithValue("@courseId", courseId);
                using (var reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        var videoId = reader.GetString("videoId");
                        var title = reader.GetString("Title");
                        result.Add(new VideoMetaData(videoId, title));
                    }
                }
            }
            return result;
        }
        
        public bool DeleteCourse(string courseId)
        {
            if (DeleteCourseFromCoursesTable(courseId))
            {
                var posterDeleted = _imageFileRepository.DeleteCoursePosterFile(courseId);
                var videosDeleted = _videoRepository.DeleteAllVideoFilesOfCourse(courseId);
                var examsDeleted = _examRepository.DeleteAllExamsOfCourse(courseId);
                if(posterDeleted && videosDeleted && examsDeleted)
                {
                    return true;
                }
            }
            return false;
        }

        public bool UpdateCourse(CourseDTO newCourse)
        {
            var query = "Update group10_courses Set Name = @Name, Description = @Description, Objectives = @Objectives Where Id = @Id";
            using (var connection = _databaseManager.GetConnection())
            {
                connection.Open();
                var command = new MySqlCommand(query, connection);
                command.Parameters.AddWithValue("@Name", newCourse.Name);
                command.Parameters.AddWithValue("@Description", newCourse.Description);
                command.Parameters.AddWithValue("@Objectives", newCourse.Objectives);
                command.Parameters.AddWithValue("@Id", newCourse.Id);
                return command.ExecuteNonQuery() > 0;
            }
        }


        //private methods : 
        private bool DeleteCourseFromCoursesTable(string courseId)
        {
            var query = "Delete From group10_courses Where Id = @courseId";
            using (var connection = _databaseManager.GetConnection())
            {
                connection.Open();
                var command = new MySqlCommand(query, connection);
                command.Parameters.AddWithValue("@courseId", courseId);
                return command.ExecuteNonQuery() > 0;
            }
        }
    }
}
