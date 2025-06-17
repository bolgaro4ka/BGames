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

from games.models import Game, Category
from BBack.settings import FRONTEND_URL
from games.serializer import GameSerializer, CategorySerializer


@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@csrf_exempt
def listOfGames(request):
    if request.method == 'POST':
        page = int(request.data['page'])
        games_on_page = int(request.data['limit'])
        category_id = int(request.data['category_id']) if ('category_id' in request.data) else None

        query = request.data['query'] if 'query' in request.data else None

        if (category_id is not None) and category_id != -1:
            games = Game.objects.filter(categories=category_id)
        else:
            games = Game.objects.all()

        if query:
            games = games.filter(name__contains=query)

        serializer = GameSerializer(games[games_on_page * (page - 1):games_on_page * page], many=True)
        return JsonResponse([{'len': len(games), 'page': page, 'limit': games_on_page, 'all_games': len(games)}] + serializer.data , safe=False)

@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@csrf_exempt
def cats(request, id):
    if request.method == 'GET':
        return JsonResponse(CategorySerializer(Category.objects.filter(id=id)[0]).data, safe=False)
    
@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@csrf_exempt
def searchGame(request):
    if request.method == 'POST':
        query = request.data['query']
        if query == '' or query == ' ':
            return JsonResponse([], safe=False)
        category = request.data['category'] if 'category' in request.data else None
        limit = request.data['limit'] if 'limit' in request.data else 10

        games_by_name = Game.objects.filter(name__contains=query)
        games_by_long_desc = Game.objects.filter(long_description__contains=query)
        games_by_short_desc = Game.objects.filter(short_description__contains=query)
        games_by_os = Game.objects.filter(os__contains=query)
        games_by_developer = Game.objects.filter(developer__contains=query)
        games_by_additional_info = Game.objects.filter(additional_info__contains=query)
        games = games_by_name | games_by_long_desc | games_by_short_desc | games_by_os | games_by_developer | games_by_additional_info

        if category is not None:
            games = games.filter(categories=category)

        serializer = GameSerializer(games[:limit], many=True)
        return JsonResponse(serializer.data, safe=False)
    
@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@csrf_exempt
def game(request, id):
    game = Game.objects.get(id=id)
    serializer = GameSerializer(game)
    return JsonResponse(serializer.data, safe=False)

@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@csrf_exempt
def len_games(request):
    return JsonResponse({'len': len(Game.objects.all())}, safe=False)

@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@csrf_exempt
def like(request):
    if Game.objects.filter(id=request.data['id']).count() == 0:
        return JsonResponse({'error': 'Game not found'}, safe=False)
    game = Game.objects.get(id=request.data['id'])
    game.likes += 1
    game.save()
    return JsonResponse(GameSerializer(game).data, safe=False)

@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@csrf_exempt
def dislike(request):
    game = Game.objects.get(id=request.data['id'])
    game.dislikes += 1
    game.save()
    return JsonResponse(GameSerializer(game).data, safe=False)

@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@csrf_exempt
def all_cats(request):
    if request.method == 'GET':
        return JsonResponse(CategorySerializer(Category.objects.all(), many=True).data, safe=False)
    