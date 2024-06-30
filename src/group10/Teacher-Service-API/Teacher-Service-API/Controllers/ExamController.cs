using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Http.HttpResults;
using Microsoft.AspNetCore.Mvc;
using Teacher_Service_API.Models.Database.Repositories;
using Teacher_Service_API.Models.DTOs;

namespace Teacher_Service_API.Controllers
{
    [Route("[controller]")]
    [ApiController]
    public class ExamController : ControllerBase
    {
        private ExamRepository _examRepository;

        public ExamController(ExamRepository examRepository)
        {
            _examRepository = examRepository;
        }

        [HttpPost("add-exam")]
        public IActionResult AddExam(ExamDTO newExam)
        {
            var id = _examRepository.AddExam(newExam);
            return Ok(id);
        }

        [HttpGet("retrieve-exams/{courseId}")]
        public IActionResult RetrieveExams(string courseId)
        {
            var exams = _examRepository.GetAllExamsOfCourse(courseId);
            return Ok(exams);
        }

        [HttpGet("get-exam/{examId}")]
        public IActionResult GetExam(string examId)
        {
            var exam = _examRepository.GetExamById(examId);
            return Ok(exam);
        }

        [HttpDelete("delete-exam/{examId}")]
        public IActionResult DeleteExam(string examId)
        {
            var result = _examRepository.DeleteExam(examId);
            if (result)
            {
                return NoContent();
            }
            return NotFound();
        }
    }
}
