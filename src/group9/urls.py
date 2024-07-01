from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("recom_title", views.recom, name="recom"),
    path("analysis_essay", views.analysis, name="correct"),
    path('simple_past/', views.Simple_past_page, name='simple_past'),
    path('present_count/', views.Present_continuous_page, name='present_count'),
    path('simple_present/', views.Simple_present_page, name='simple_present'),
    path('present_perfect/', views.Present_perfect_page, name='present_perfect'),
    path('past_count/', views.Past_continuous_page, name='past_count'),
    path('future_simple/', views.Future_simple_page, name='future_simple'),
    path('speaking_bank1/', views.speaking_bank1, name='speaking_bank1'),
    path('speaking_bank2/', views.speaking_bank2, name='speaking_bank2'),
    path('speaking_bank3/', views.speaking_bank3, name='speaking_bank3'),
    path('first/', views.first_page, name='first'),


] 

