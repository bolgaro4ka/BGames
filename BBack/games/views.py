from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import authentication_classes

from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
import requests
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes

from games.models import Game
from BBack.settings import FRONTEND_URL
from games.serializer import GameSerializer


@api_view(('GET', 'POST'))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@csrf_exempt
def listOfGames(request, page=1, games_on_page=10):
    if request.method == 'GET':
        games = Game.objects.all()[games_on_page * (page - 1):games_on_page * page]
        serializer = GameSerializer(games, many=True)
        return JsonResponse([{'len': len(games), 'page': page, 'games_on_page': games_on_page}] + serializer.data , safe=False)

    
@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@csrf_exempt
def searchGame(request):
    if request.method == 'POST':
        query = request.data['query']
        category = request.data['category'] if 'category' in request.data else None

        games_by_name = Game.objects.filter(name__contains=query)
        games_by_long_desc = Game.objects.filter(long_description__contains=query)
        games_by_short_desc = Game.objects.filter(short_description__contains=query)
        games_by_os = Game.objects.filter(os__contains=query)
        games_by_developer = Game.objects.filter(developer__contains=query)
        games_by_additional_info = Game.objects.filter(additional_info__contains=query)
        games = games_by_name | games_by_long_desc | games_by_short_desc | games_by_os | games_by_developer | games_by_additional_info

        if category is not None:
            games = games.filter(categories=category)

        serializer = GameSerializer(games, many=True)
        return JsonResponse(serializer.data, safe=False)
    
@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@csrf_exempt
def game(request, id):
    game = Game.objects.get(id=id)
    serializer = GameSerializer(game)
    return JsonResponse(serializer.data, safe=False)