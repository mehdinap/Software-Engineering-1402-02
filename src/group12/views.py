import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Reading, Question

@csrf_exempt
def send_create_exam_request(request):
    if request.method == 'POST':
        flask_url = 'http://localhost:5000/createExam'
        data = {
            'level': request.POST.get('level')
        }
        response = requests.post(flask_url, data=data)
        try:
            response.raise_for_status()
            flask_response = response.json()

            readings = []
            for reading_data in flask_response['readings']:
                reading = Reading(
                    level=reading_data['level'],
                    content=reading_data['content'],
                    translation=reading_data['translation']
                )
                print(reading)
                reading.save()

                questions = []
                for question_data in reading_data['questions']:
                    question = Question(
                        content=question_data['content'],
                        choice1=question_data['choice1'],
                        choice2=question_data['choice2'],
                        choice3=question_data['choice3'],
                        choice4=question_data['choice4'],
                        correct_choice=question_data['correct_choice'],
                        reading=reading
                    )
                    
                    question.save()
                    questions.append(question)

                reading.questions.add(*questions)
        
                readings.append(reading)

            return render(request, 'group12/myapp/ExamPage.html', {'readings': readings})
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return JsonResponse({'error': 'Request to Flask server failed'}, status=500)
        except requests.exceptions.JSONDecodeError as e:
            print(f"JSON decode failed: {e}")
            return JsonResponse({'error': 'Invalid JSON response from Flask server'}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)



@csrf_exempt
def send_create_practice_request(request):
    if request.method == 'POST':
        flask_url = 'http://localhost:5000/createPractice'
        data = {
            'level': request.POST.get('practice-level'),
            'number-of-readings': request.POST.get('number-of-readings')
        }
        try:
            response = requests.post(flask_url, data=data)
            response.raise_for_status()
            flask_response = response.json()
            print(flask_response)

            readings = []
            for reading_data in flask_response['readings']:
                reading = Reading(
                    level=reading_data['level'],
                    content=reading_data['content'],
                    translation=reading_data['translation']
                )
                reading.save()

                questions = []
                for question_data in reading_data['questions']:
                    question = Question(
                        content=question_data['content'],
                        choice1=question_data['choice1'],
                        choice2=question_data['choice2'],
                        choice3=question_data['choice3'],
                        choice4=question_data['choice4'],
                        correct_choice=question_data['correct_choice'],
                        reading=reading
                    )
                    question.save()
                    questions.append(question)

                reading.questions.add(*questions)
                readings.append(reading)

            return render(request, 'group12/myapp/PracticePage.html', {'readings': readings})
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return JsonResponse({'error': 'Request to Flask server failed'}, status=500)
        except requests.exceptions.JSONDecodeError as e:
            print(f"JSON decode failed: {e}")
            return JsonResponse({'error': 'Invalid JSON response from Flask server'}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def index(request):
    if request.method == 'GET':
        flask_url = 'http://localhost:5000/'
        try:
            response = requests.get(flask_url)
            response.raise_for_status()
            flask_response = response.json()
            return render(request, 'group12/myapp/BasePage.html', {'data': flask_response})
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return JsonResponse({'error': 'Request to Flask server failed'}, status=500)
        except requests.exceptions.JSONDecodeError as e:
            print(f"JSON decode failed: {e}")
            return JsonResponse({'error': 'Invalid JSON response from Flask server'}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def setup_page(request):
    if request.method == 'GET':
        flask_url = 'http://localhost:5000/SetupPage'
        try:
            response = requests.get(flask_url)
            response.raise_for_status()
            flask_response = response.json()
            return render(request, 'group12/myapp/SetupPage.html', {'data': flask_response})
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return JsonResponse({'error': 'Request to Flask server failed'}, status=500)
        except requests.exceptions.JSONDecodeError as e:
            print(f"JSON decode failed: {e}")
            return JsonResponse({'error': 'Invalid JSON response from Flask server'}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
