
from django.urls import path,include
from .views import home, get_quiz,quiz,submit_quiz

urlpatterns = [
    path('', home, name='home'),
    path('api/get-quiz/', get_quiz, name='get_quiz'),
    path('quiz/', quiz, name='quiz'),
    path('submit-quiz/', submit_quiz, name='submit_quiz'),
]
