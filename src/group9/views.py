from django.shortcuts import render
from django import forms
from . import tests as app

# Create your views here.


class TitleForm(forms.Form):
    title = forms.CharField(label="userTitle")
class AnalysisForm(forms.Form):
    essay_form = forms.CharField(label="userEssay")
class UploadFileForm(forms.Form):
    file = forms.FileField()

def index(request):
    # f= request.GET['audio_file']
    # if request.FILES['file']:
    #     print("print in index")    
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print("is valid")

        
    return render(request, "./index.html",)
    
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
    context = {}
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
    context['section_id'] = "writing_page"
    return render(request, './index.html', context)
    

def upload_file(request):
    print("in voice")
    context={}
    context['section_id'] = "speaking_page"
    if request.method == 'POST':
        uploaded_file = request.FILES['audio_file']
        text = app.audio_to_text(uploaded_file)
        analysis = app.analysis_essay(text)
        context['analysis_result'] = analysis
        return render(request, './index.html', context)
    else:

        return render(request, './index.html',context)
    


# def upload_file(request):
#     if request.method == 'POST' and request.FILES['file']:
#         uploaded_file = request.FILES['file']
        
#         # Process the uploaded file (e.g., save it to a specific location)
#         with open('path/to/save/file.txt', 'wb+') as destination:
#             for chunk in uploaded_file.chunks():
#                 destination.write(chunk)
        
#         return render(request, 'upload_success.html')
    
#     return render(request, 'upload_form.html')