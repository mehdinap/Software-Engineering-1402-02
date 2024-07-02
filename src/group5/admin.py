from django.contrib import admin
from .models import Part, Word, Category, Exam, Question
# Register your models here.

admin.site.register(Part)
admin.site.register(Category)
admin.site.register(Word)
admin.site.register(Question)
admin.site.register(Exam)
