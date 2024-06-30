from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('listening/', views.listening_test, name='listening_test'),
    path('submit_listening/', views.submit_listening_test, name='submit_listening_test'),
    path('reading/', views.reading_test, name='reading_test'),
    path('reading/', views.reading_test, name='reading_test'),
    path('submit_reading/', views.submit_reading_test, name='submit_reading_test'),
    path('writing/part1/', views.writing_test_part1, name='writing_test_part1'),
    path('writing/part2/', views.writing_test_part2, name='writing_test_part2'),
    path('', views.home, name='home'),
    path('speaking/', views.speaking_test, name='speaking_test'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

