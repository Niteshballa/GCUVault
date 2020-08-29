from django.contrib import admin
from django.urls import path
from . import views
app_name="quiz"
urlpatterns=[
    path('quiztime',views.quiztime,name="quiztime"),
    path('weeklyquiz',views.weeklyquiz,name="weeklyquiz"),
    path('weekendquiz',views.weekendquiz,name="weekendquiz"),
    path('winners',views.winner,name="winners"),
    path('contests',views.contest,name="contests"),
    path('quizend',views.quizend,name="quizend"),
    path('quizparticipated',views.quizparticipated,name="quizparticipated"),
    path('quizover',views.quizover,name="quizover"),
]