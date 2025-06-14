from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import *

urlpatterns = [
    path("len/", len_games),
    path("like/", like),
    path("dislike/", dislike),
    path("list/", listOfGames),
    path("search/", searchGame),
    path("cat/<int:id>/", cats),
    path("<str:id>/", game),
    
]
