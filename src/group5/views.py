from django.shortcuts import render, redirect
from .models import Category, Part, Word, Question, Exam
from .utility import WordListProxy


# Create your views here.

def show_categories(request):
    categories = Category.objects.all()
    
    return render(request, 'tutorials/categories.html', {'categories': categories, 'title': 'Categories', 'url_name': 'show_parts'})


def show_parts(request, category_id: int):
    parts = Part.objects.filter(category__id=category_id)
    
    return render(request, 'tutorials/categories.html', {'categories': parts, 'title': 'Parts',  'url_name': 'show_words'})


def show_words(request, part_id: int):
    words = Word.objects.filter(part__id=part_id)
    
    return render(request, 'tutorials/words.html', {'words': words})


def exam(request):
    user = request.user

    if user is not None and user.is_authenticated:
        words = Word.objects.all()
        proxy = WordListProxy(words)
        exam = Exam(user=user, result=0)
        # exam.save()
        questions_count = min(len(words), 4)

        class Test:
            def __init__(self, question, choices) -> None:
                self.question = question
                self.choices = choices
        
        questions = []
        for i in range(int(questions_count / 2)):
            word, definition, choices = proxy.select_random_word_with_three_definitions()
            question = Question(text=f"Select the correct definition for '{word}'", answer=definition)
            # question.save()
            questions.append(Test(question, choices))

            word, definition, choices = proxy.choose_random_definition_with_three_words()
            question = Question(text=f"Which one is the word for '{definition}'", answer=word)
            # question.save()
            questions.append(Test(question, choices))

        return render(request, 'exam/index.html', {'questions': questions})
    
    return redirect('login')