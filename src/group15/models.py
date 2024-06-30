from django.db import models

class ListeningQuestion(models.Model):
    audio_file = models.FileField(upload_to='audio/')
    question_text = models.TextField()
    correct_answer = models.TextField()

class ReadingQuestion(models.Model):
    passage_text = models.TextField()
    question_text = models.TextField()
    correct_answer = models.TextField()

class WritingTask(models.Model):
    task_number = models.IntegerField()
    question_text = models.TextField()

class SpeakingQuestion(models.Model):
    PART_CHOICES = [
        (1, 'Part 1'),
        (2, 'Part 2'),
        (3, 'Part 3'),
    ]
    part = models.IntegerField(choices=PART_CHOICES, default=1)
    question_text = models.TextField()
    def __str__(self):
        return f"Part {self.part}: {self.question_text}"