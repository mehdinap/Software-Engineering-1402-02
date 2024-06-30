from django.db import models


# Create your models here.
class Video:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.video_file = None

    def set_video_file(self, video_file):
        self.video_file = video_file


class Course:
    def __init__(self, name, description, objectives, id):
        self.name = name
        self.description = description
        self.objectives = objectives
        self.id = id
        self.image_data = None

    def set_image(self, image_data):
        self.image_data = image_data


class Exam:
    def __init__(self, name, subjects, course_id, exam_id):
        self.name = name
        self.subjects = subjects
        self.course_id = course_id
        self.exam_id = exam_id


class Question:
    def __init__(self, test_id, id, question, option1, option2, option3, option4, category):
        self.test_id = test_id
        self.id = id
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.category = category
