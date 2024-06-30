using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Teacher_Service_API.Models.Database.Repositories;
using Teacher_Service_API.Models.DTOs;

namespace Teacher_Service_API.Controllers
{
    [Route("[controller]")]
    [ApiController]
    public class CourseController : ControllerBase
    {
        private readonly TeacherRepository _teacherRepository;
        private readonly CourseRepository _courseRepository;
        private readonly VideoFileRepository _videoFileRepository;
        private readonly ImageFileRepository _imageFileRepository;
        public CourseController(TeacherRepository teacherRepository, CourseRepository courseRepository, VideoFileRepository videoFileRepository, ImageFileRepository imageFileRepository)
        {
            _teacherRepository = teacherRepository;
            _courseRepository = courseRepository;
            _videoFileRepository = videoFileRepository;
            _imageFileRepository = imageFileRepository;
        }

        [HttpPost("add-course/{teacherEmail}")]
        public IActionResult AddCourse(string teacherEmail, [FromBody] CourseDTO newCourse)
        {
            var teacherId = _teacherRepository.GetIdByEmail(teacherEmail);
            var teacher = _teacherRepository.GetTeacherById(teacherId);
            var result = teacher.AddCourse(newCourse);
            
            if (result != null)
            {
                return Ok(result.Id);
            }
            else
            {
                return BadRequest();
            }
        }

        [HttpGet("get-teacher-courses/{teacherEmail}")]
        public IActionResult GetAllTeacherCourses(string teacherEmail)
        {
            var teacherId = _teacherRepository.GetIdByEmail(teacherEmail);
            var courses = _courseRepository.GetAllCoursesOfTeacher(teacherId);
            if ( courses == null)
            {
                return BadRequest();
            }
            else if ( courses.Count() == 0)
            {
                return NotFound();
            }
            else
            {
                return Ok(courses);
            }
        }

        [HttpGet("get-course/{id}")]
        public IActionResult GetCourseById(string id)
        {
            return Ok(_courseRepository.GetCourseById(id));
        }


        [HttpGet("get_videos_metadata/{courseId}")]
        public IActionResult GetVideosMetadata(string courseId)
        {
            var videosIds = _courseRepository.GetCourseVideosMetaData(courseId);
            return Ok(videosIds);
        }

        [HttpDelete("delete-course/{courseId}")]
        public IActionResult DeleteCourse(string courseId)
        {

            var result = _courseRepository.DeleteCourse(courseId);
            if (result)
            {
                return NoContent();
            }
            return NotFound();
        }

        [HttpDelete("delete-video/{videoId}")]
        public IActionResult DeleteVideo(string videoId)
        {
            var result = _videoFileRepository.DeleteVideo(videoId);
            if(result)
            {
                return NoContent();
            }
            return NotFound();
        }
    }
}
