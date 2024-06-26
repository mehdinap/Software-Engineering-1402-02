# group14/views.py

from django.shortcuts import render
from django.http import HttpResponse
from database.query import create_db_connection, get_posts_by_user_id
from database.secret import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

# Create your views here.
def home(request):
    return render(request, 'group14/home.html')
