from django.urls import path
from . import views


urlpatterns = [
  
     path('group12', views.index, name='index'),
    path('SetupPage/', views.setup_page, name='setup_page'),
    path('create-exam/', views.send_create_exam_request, name='create_exam'),
    path('create-practice/', views.send_create_practice_request, name='create_practice'),
]
