from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ListeningQuestion, ReadingQuestion, WritingTask, SpeakingQuestion
from .forms import WritingAnswerForm, ReadingAnswerForm, ListeningAnswerForm
from django.views.decorators.http import require_POST

def home(request):
    return render(request, 'home.html')

def listening_test(request):
    questions = ListeningQuestion.objects.all()
    return render(request, '../templates/tests/listening_test.html', {'questions': questions})

@require_POST
def submit_listening_test(request):
    questions = ListeningQuestion.objects.all()
    user_answers = {}
    correct_answers = {}

    for question in questions:
        answer_key = f"answer_{question.id}"
        user_answers[question.id] = request.POST.get(answer_key, "")
        correct_answers[question.id] = question.correct_answer

    score = sum(1 for question_id, user_answer in user_answers.items() if user_answer == correct_answers.get(question_id, ""))
    return render(request, '../templates/tests/listening_result.html', {'score': score, 'correct_answers': correct_answers})


def reading_test(request):
    # Fetch the passage text and questions
    questions = ReadingQuestion.objects.all()
    passage_text = questions.first().passage_text if questions.exists() else ""
    
    # Render the reading test form
    return render(request, '../templates/tests/reading_test.html', {'passage_text': passage_text, 'questions': questions})

@require_POST
def submit_reading_test(request):
    # Fetch all questions for processing answers
    questions = ReadingQuestion.objects.all()
    
    # Prepare to collect user answers and correct answers
    user_answers = {}
    correct_answers = {}
    
    for question in questions:
        answer_key = f"answer_{question.id}"
        user_answers[question.id] = request.POST.get(answer_key, "")
        correct_answers[question.id] = question.correct_answer
    
    # Example: Calculate score based on correct answers
    score = sum(1 for question_id, user_answer in user_answers.items() if user_answer == correct_answers.get(question_id, ""))

    # Render the result page with score and correct answers
    return render(request, '../templates/tests/reading_result.html', {'score': score, 'correct_answers': correct_answers})

def writing_test_part1(request):
    task = WritingTask.objects.get(task_number=1)  # Assuming WritingTask model has tasks 1 and 2
    form = WritingAnswerForm()

    if request.method == 'POST':
        form = WritingAnswerForm(request.POST)
        if form.is_valid():
            # Process the form data for part 1, maybe save to database, etc.
            answer_part1 = form.cleaned_data['answer']
            # Redirect to part 2
            return redirect('writing_test_part2')

    return render(request, '../templates/tests/writing_test_part1.html', {'task': task, 'form': form})

def writing_test_part2(request):
    task = WritingTask.objects.get(task_number=2)  # Assuming WritingTask model has tasks 1 and 2
    form = WritingAnswerForm()

    if request.method == 'POST':
        form = WritingAnswerForm(request.POST)
        if form.is_valid():
            # Process the form data for part 2, maybe save to database, etc.
            answer_part2 = form.cleaned_data['answer']
            # Redirect to home or any other page after test ends
            return redirect('home')

    return render(request, '../templates/tests/writing_test_part2.html', {'task': task, 'form': form})


def speaking_test(request):
    part1_questions = SpeakingQuestion.objects.filter(part=1)
    part2_questions = SpeakingQuestion.objects.filter(part=2)
    part3_questions = SpeakingQuestion.objects.filter(part=3)
    context = {
        'part1_questions': part1_questions,
        'part2_questions': part2_questions,
        'part3_questions': part3_questions
    }
    return render(request, '../templates/tests/speaking_test.html', context)
