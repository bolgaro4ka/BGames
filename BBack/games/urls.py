from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import *

urlpatterns = [
    path("list/<int:page>/<int:games_on_page>/", listOfGames),
    path("search/", searchGame),
    path("<str:id>/", game),
]
