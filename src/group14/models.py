from django.db import models

# Create your models here.
class Card(models.Model):
    id = models.AutoField(primary_key=True)
    front_value = models.CharField(max_length=255)
    back_value = models.CharField(max_length=255)
    box_number = models.IntegerField()
    # user = models.ForeignKey(Users, on_delete=models.CASCADE)
    last_review = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

