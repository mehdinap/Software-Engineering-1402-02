from django.db import models


class Reading(models.Model):
    level = models.IntegerField()
    content = models.TextField()
    translation = models.TextField()

    def __str__(self):
        return f'Reading {self.id}'

class Question(models.Model):
    content = models.TextField()
    choice1 = models.CharField(max_length=200)
    choice2 = models.CharField(max_length=200)
    choice3 = models.CharField(max_length=200)
    choice4 = models.CharField(max_length=200)
    correct_choice = models.CharField(max_length=200)
    reading = models.ForeignKey(Reading, on_delete=models.CASCADE, related_name='questions')
    

    def __str__(self):
        return f'Question {self.id}'
