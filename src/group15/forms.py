from django import forms
from .models import WritingTask

class WritingAnswerForm(forms.Form):
    answer = forms.CharField(widget=forms.Textarea, max_length=1000, label='Your Answer')

class ReadingAnswerForm(forms.Form):
    answer = forms.CharField(widget=forms.Textarea, max_length=500)

class ListeningAnswerForm(forms.Form):
    answer = forms.CharField(widget=forms.Textarea, max_length=500)
