from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import authentication_classes

from rest_framework.response import Response

from bs4 import BeautifulSoup
import requests

from BBack.settings import FRONTEND_URL


@api_view(['GET'])
# Create your views here.
def listOfGames(request, category, page):
    if category == 'empty':
        soup = BeautifulSoup(requests.get(f'https://thelastgame.ru/page/{page}').text, 'html.parser')
    else:
        soup = BeautifulSoup(requests.get(f'https://thelastgame.ru/category/{category}/page/{page}').text, 'html.parser')
    ans = {}
    for article in soup.find_all('article'):

        name = article.find('h2', class_='post-title').find('a').text
        image = article.find('div', class_='post-thumbnail').find('a').find('img').attrs["data-srcset"].split(', ')[0].split(' ')[0]
        description = article.find('div', class_='entry-summary').find('p').text
        lurl = article.find('h2', class_='post-title').find('a').attrs["href"]
        burl = FRONTEND_URL + lurl.replace('https://thelastgame.ru/', '')

        groups = [item for item in article.find('div', class_='post-meta').find_all('a') if 'group' in item.attrs['href']]
        if groups:
            group = groups[0].text
        else:
            group = ''

        ans[name] = {'image': image, 'desc': description, 'last_url': lurl, 'url': burl}

    
    return Response({'html': str(ans)})