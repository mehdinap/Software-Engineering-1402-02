from django.urls import path
from . import views


urlpatterns = [
    path('', view=views.show_categories, name='home'),
    path('categories/<int:category_id>/', view=views.show_parts, name='show_parts'),
    path('parts/<int:part_id>/', view=views.show_words, name='show_words'),
    path('exam', view=views.exam, name='exam'),
] 
