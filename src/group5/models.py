from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Part(models.Model):
    category = models.ForeignKey(Category, related_name='parts', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Word(models.Model):
    part = models.ForeignKey(Part, related_name='words', on_delete=models.CASCADE)
    exact_word = models.CharField(max_length=100)
    definition = models.TextField()
    image = models.ImageField(upload_to='word_images/')

    def image_url(self):
        return self.image.url
        
    def __str__(self):
        return self.exact_word



class Exam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    result = models.FloatField()


class Question(models.Model):
    text = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

    user_answer = models.CharField(max_length=200)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, blank=False)
