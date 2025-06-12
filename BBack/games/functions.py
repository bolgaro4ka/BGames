from bs4 import BeautifulSoup
import requests
from BBack.settings import FRONTEND_URL

from games.models import Game, Category


def updateGames():
    for page in range(1, 10):  #846
        ans = {}
        soup = BeautifulSoup(requests.get(f'https://thelastgame.ru/page/{page}').text, 'html.parser')
        for article in soup.find_all('article'):

            name = article.find('h2', class_='post-title').find('a').text
            image = article.find('div', class_='post-thumbnail').find('a').find('img').attrs["data-srcset"].split(', ')[0].split(' ')[0]
            description = article.find('div', class_='entry-summary').find('p').text
            lurl = article.find('h2', class_='post-title').find('a').attrs["href"]
            burl = FRONTEND_URL + lurl.replace('https://thelastgame.ru/', '')
            try:
                groups = [[item.attrs["href"].replace('https://thelastgame.ru/category/', '').split('/')[0], item.text] for item in article.find('p', class_='post-category').find_all('a')]
            except:
                groups = []

            ans[name] = {'image': image, 'desc': description, 'last_url': lurl, 'url': burl, 'groups': groups}

            page_soup = BeautifulSoup(requests.get(lurl).text, 'html.parser')

            try:
                long_desc = page_soup.find('div', class_='entry-inner').find('p').text
            except:
                long_desc = ''

            images = page_soup.find('div', id="gamepics").find_all('a')


            info_game = page_soup.find('div', class_='entry-inner').find_all('div')[2].text[18:].split('\n')
            try:
                year = info_game[0].split(': ')[1]
            except Exception as e:
                year = ''
                print(name, e)

            try:
                genre = info_game[1].split(': ')[1]
            except Exception as e:
                genre = ''
                print(name, e)

            try:
                dev = info_game[2].split(': ')[1]
            except Exception as e:
                dev = ''
                print(name, e)

            try:
                version = info_game[3].split(': ')[1]
            except Exception as e:
                version = ''
                print(name, e)

            try:
                language = info_game[4].split(': ')[1]
            except Exception as e:
                language = ''
                print(name, e)

            try:
                tablet = info_game[5].split(': ')[1]
            except Exception as e:
                tablet = ''
                print(name, e)

            requiments = page_soup.find('div', class_='entry-inner').find_all('div')[3].text[33:].split('\n')
            try:
                os = requiments[0].split(': ')[1]
            except Exception as e:
                os = ''
                print(name, e)

            try:
                cpu = requiments[1].split(': ')[1]
            except Exception as e:
                cpu = ''
                print(name, e)

            try:
                ram = requiments[2].split(': ')[1]
            except Exception as e:
                ram = ''
                print(name, e)

            try:
                gpu = requiments[3].split(': ')[1]
            except Exception as e:
                gpu = ''
                print(name, e)

            try:
                size = requiments[4].split(': ')[1]
            except Exception as e:
                size = ''
                print(name, e)

            try:
                add_block = page_soup.find('div', class_='entry-inner').find_all('div')[5].text[6:]
            except:
                add_block = ''

            try:
                download_url = page_soup.find('a', class_='btn_green').attrs['href']
            except Exception as e:
                download_url = ''
                print(name, e)
            
            try:
                pic1_url = images[0].attrs["href"]
            except Exception as e:
                pic1_url = ''
                print(name, e)


            try:
                pic2_url = images[1].attrs["href"]
            except Exception as e:
                pic2_url = ''
                print(name, e)

            try:
                pic3_url = images[2].attrs["href"]
            except Exception as e:
                pic3_url = ''
                print(name, e)

            ans[name]['long_desc'] = long_desc

            ans[name]['pic1_url'] = pic1_url
            ans[name]['pic2_url'] = pic2_url
            ans[name]['pic3_url'] = pic3_url

            ans[name]['year'] = year
            ans[name]['genre'] = genre
            ans[name]['developer'] = dev
            ans[name]['version'] = version
            ans[name]['language'] = language
            ans[name]['tablet'] = tablet

            ans[name]['os'] = os
            ans[name]['cpu'] = cpu
            ans[name]['ram'] = ram
            ans[name]['gpu'] = gpu
            ans[name]['size'] = size

            ans[name]['download_url1'] = download_url

            ans[name]['additional_info'] = add_block

        

        for game in ans.keys():
            cats=[]
            for category in ans[game]['groups']:
                try:
                    cat = Category.objects.get(short_name=category[0])
                except:
                    cat = Category.objects.create(name=category[1], short_name=category[0])
                    cat.save()
                cats.append(cat)

            lgame = Game.objects.filter(name=game)
            if lgame.exists():
                lgame[0].name = game
                lgame[0].image_url = ans[game]['image'] if ans[game]['image'] else lgame[0].image_url
                lgame[0].short_description = ans[game]['desc'] if ans[game]['desc'] else lgame[0].short_description
                lgame[0].game_url = ans[game]['url'] if ans[game]['url'] else lgame[0].game_url
                lgame[0].long_description = ans[game]['long_desc'] if ans[game]['long_desc'] else lgame[0].long_description
                lgame[0].pic1_url = ans[game]['pic1_url'] if ans[game]['pic1_url'] else lgame[0].pic1_url
                lgame[0].pic2_url = ans[game]['pic2_url'] if ans[game]['pic2_url'] else lgame[0].pic2_url
                lgame[0].pic3_url = ans[game]['pic3_url'] if ans[game]['pic3_url'] else lgame[0].pic3_url
                lgame[0].year = ans[game]['year'] if ans[game]['year'] else lgame[0].year
                lgame[0].genre = ans[game]['genre'] if ans[game]['genre'] else lgame[0].genre
                lgame[0].developer = ans[game]['developer'] if ans[game]['developer'] else lgame[0].developer
                lgame[0].version = ans[game]['version'] if ans[game]['version'] else lgame[0].version
                lgame[0].language = ans[game]['language'] if ans[game]['language'] else lgame[0].language
                lgame[0].tablet = ans[game]['tablet'] if ans[game]['tablet'] else lgame[0].tablet
                lgame[0].os = ans[game]['os'] if ans[game]['os'] else lgame[0].os
                lgame[0].cpu = ans[game]['cpu'] if ans[game]['cpu'] else lgame[0].cpu
                lgame[0].ram = ans[game]['ram'] if ans[game]['ram'] else lgame[0].ram
                lgame[0].gpu = ans[game]['gpu'] if ans[game]['gpu'] else lgame[0].gpu
                lgame[0].size = ans[game]['size'] if ans[game]['size'] else lgame[0].size
                lgame[0].download_url1 = ans[game]['download_url1'] if ans[game]['download_url1'] else lgame[0].download_url1
                lgame[0].additional_info = ans[game]['additional_info'] if ans[game]['additional_info'] else lgame[0].additional_info

                
                lgame[0].categories.clear()
                for cat in cats:
                    lgame[0].categories.add(cat)


                lgame[0].save()
            else:
                lgame = Game.objects.create(
                    name=game,
                    image_url=ans[game]['image'],
                    short_description=ans[game]['desc'],
                    game_url=ans[game]['url'],
                    long_description=ans[game]['long_desc'],
                    pic1_url=ans[game]['pic1_url'],
                    pic2_url=ans[game]['pic2_url'],
                    pic3_url=ans[game]['pic3_url'],
                    year=ans[game]['year'],
                    genre=ans[game]['genre'],
                    developer=ans[game]['developer'],
                    version=ans[game]['version'],
                    language=ans[game]['language'],
                    tablet=ans[game]['tablet'],
                    os=ans[game]['os'],
                    cpu=ans[game]['cpu'],
                    ram=ans[game]['ram'],
                    gpu=ans[game]['gpu'],
                    size=ans[game]['size'],
                    download_url1=ans[game]['download_url1'],
                    additional_info=ans[game]['additional_info'],
                )

                for cat in cats:
                    lgame.categories.add(cat)

                lgame.save()

        print(f'{page} |')

# from games.functions import *; updateGames()