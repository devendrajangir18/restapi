from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
        path('student/', StudentAPI.as_view()),
        path('register/', RegisterUser.as_view()),
        # path('get-book'/, get_book),
        # path('', home),
        # path('student/', post_student)

]
