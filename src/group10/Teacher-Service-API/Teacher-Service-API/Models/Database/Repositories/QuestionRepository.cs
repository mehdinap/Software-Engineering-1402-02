using MySql.Data.MySqlClient;
using Teacher_Service_API.Models.DTOs;

namespace Teacher_Service_API.Models.Database.Repositories
{
    public class QuestionRepository
    {
        private readonly DatabaseManager _databaseManager = new DatabaseManager();

        public void AddQuestion(QuestionDTO questionDTO)
        {
            var query = "insert into group10_questions(testId,id,question,category,option1,option2,option3,option4) values (@testId,@id,@question,@category,@option1,@option2,@option3,@option4)";
            var id = Guid.NewGuid().ToString();
            using (var connection = _databaseManager.GetConnection())
            {
                connection.Open();
                var command = new MySqlCommand(query, connection);
                command.Parameters.AddWithValue("@testId", questionDTO.TestId);
                command.Parameters.AddWithValue("@id", id);
                command.Parameters.AddWithValue("@question", questionDTO.Question);
                command.Parameters.AddWithValue("@category", questionDTO.Category);
                command.Parameters.AddWithValue("@option1", questionDTO.Option1);
                command.Parameters.AddWithValue("@option2", questionDTO.Option2);
                command.Parameters.AddWithValue("@option3", questionDTO.Option3);
                command.Parameters.AddWithValue("@option4", questionDTO.Option4);
                command.ExecuteNonQuery();
            }
        }

        public List<QuestionDTO> GetQuestionsOfExam(string testId)
        {
            var result = new List<QuestionDTO>();
            var query = "select * from group10_questions where testId = @testId";
            using (var connection = _databaseManager.GetConnection())
            {
                connection.Open();
                var command = new MySqlCommand(query, connection);
                command.Parameters.AddWithValue("@testId", testId);
                using (var reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        var id = reader.GetString(1);
                        var question = reader.GetString(2);
                        var category = reader.GetString(3);
                        var option1 = reader.GetString(4);
                        var option2 = reader.GetString(5);
                        var option3 = reader.GetString(6);
                        var option4 = reader.GetString(7);
                        result.Add(new QuestionDTO(testId, id, question, category, option1, option2, option3, option4));
                    }
                }
            }
            return result;
        }

        public bool DeleteQuestion(string questionId)
        {            
            var query = "delete from group10_questions where id = @id";
            using (var connection = _databaseManager.GetConnection())
            {
                connection.Open();
                var command = new MySqlCommand(query, connection);
                command.Parameters.AddWithValue("@id", questionId);
                return command.ExecuteNonQuery() > 0;
            }
        }

        public bool DeleteAllQuestionsOfExam(string testId)
        {
            var result = true;
            var query = "select * from group10_questions where testId = @testId";
            using (var connection = _databaseManager.GetConnection())
            {
                connection.Open();
                var command = new MySqlCommand(query, connection);
                command.Parameters.AddWithValue("@testId", testId);
                using (var reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        var id = reader.GetString(1);
                        if (!DeleteQuestion(id))
                        {
                            result = false;
                        }
                    }
                    return result;
                }
            }
        }
    }
}
