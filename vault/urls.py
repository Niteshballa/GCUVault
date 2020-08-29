from django.contrib import admin
from django.urls import path
from . import views

app_name="vault"
urlpatterns=[
     path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('about',views.about,name="about"),
    path('latest',views.latest,name="latest"),
    path('latestnetflix',views.latestnetflix,name="latest-netflix"),
    path('latestprime',views.latestprime,name="latest-prime"),
    path('latestnetflixseries',views.latestnetflixseries,name="latestnetflixseries"),
    path('latestprimeseries',views.latestprimeseries,name="latestprimeseries"),
    path('upcoming',views.upcoming,name="upcoming"),
    path('upcomingnetflix',views.upcomingnetflix,name="upcoming-netflix"),
    path('upcomingprime',views.upcomingprime,name="upcoming-prime"),
    path('upcomingnetflixseries',views.upcomingnetflixseries,name="upcomingnetflixseries"),
    path('upcomingprimeseries',views.upcomingprimeseries,name="upcomingprimeseries"),
    path('suggestion',views.suggestions,name="Suggestions"),
    path('mvesuggestion',views.mvesuggestion,name="Movie-Vault"),
    path('wbssuggestion',views.wbssuggestion,name="TV-Vault"),
    path('anime',views.topanime,name="topanime"),
    path('toprated',views.toprated,name="Top-rated"),
    path('trending',views.trending,name="Trending"),
    path('trendingseries',views.trendingseries,name="Trending Series"),
    path('article/<str:id>',views.article,name="article"),
    path('articles',views.articles,name="articles"),
    path('weeksuggestions/<str:id>',views.weeksuggestions,name="weeksuggestions"),
    path('movie/<str:id>',views.movie,name="movie"),
    path('tv/<str:id>',views.tv,name="tv"),
    path('anime/<str:id>',views.anime,name="anime"),
    path('latestprimeseries',views.latestprimeseries,name="latestprimeseries"),
    path('upcomingnetflixseries',views.upcomingnetflixseries,name="upcomingnetflixseries"),
    path('upcomingprimeseries',views.upcomingprimeseries,name="upcomingprimeseries"),
    

]