from django.shortcuts import render
from django import forms
from . import tests as app
# Create your views here.


class TitleForm(forms.Form):
    title = forms.CharField(label="userTitle")
class AnalysisForm(forms.Form):
    essay_form = forms.CharField(label="userEssay")


def index(request):

    latest_question_list = "hello world"
    context = {"latest_question_list": latest_question_list}
        
    return render(request, "./index.html", context)
    
def Simple_past_page(request):
    return render(request, "./simple_past.html")
def Present_continuous_page(request):
    return render(request, "./present_count.html")
def Simple_present_page(request):
    return render(request, "./simple_present.html")
def Present_perfect_page(request):
    return render(request, "./present_perfect.html")
def Past_continuous_page(request):
    return render(request, "./past_count.html")
def Future_simple_page(request):
    return render(request, "./future_simple.html")
def speaking_bank1(request):
    return render(request, "./speaking_bank1.html")
def speaking_bank2(request):
    return render(request, "./speaking_bank2.html")
def speaking_bank3(request):
    return render(request, "./speaking_bank3.html")
def first_page(request):
    return render(request, "./menu _bank.html")

def recom(request):
    print("in post")
    if request.method == "POST":
        
        form = TitleForm(request.POST)
        title = form.data['userTitle']
        # print("title :\n", title )
        titles = app.recommend_title(title)
        context = {'title': title, 'titles': titles}
        return render(request, './index.html', context)


def analysis (request):
    if request.method == "POST":
        
        form = AnalysisForm(request.POST)
        essay = form.data['userEssay']
        # print("essay :\n", essay )
        analysis = app.analysis_essay(essay)
        context = {'essay': essay, 'analysis': analysis}
        result = analysis.lower()
        if "present" in result : 
            context['Simple_present'] = "Simple present"
            context['Present_continuous'] = "Present continuous"
            context['Present_perfect'] = "Present perfect"
        
        if "past" in result:
            context['Past_continuous'] = "Past continuous"
            context['Simple_past'] = "Simple past"

        if "future" in result:
            context['Future_simple'] = "Future simple"
        
        return render(request, './index.html', context)
    pass