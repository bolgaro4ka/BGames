from rest_framework import serializers
from games.models import Game, Category, Comment


class GameSerializer(serializers.ModelSerializer):
     class Meta:
        model = Game
        fields = ['id', 'name', 'categories', 'image_url', 'game_url', 'short_description',
                  'long_description', 'year', 'developer', 'version', 'language', 'tablet', 'genre', 'os', 'cpu',
                  'ram', 'gpu', 'size', 'additional_info', 'pic1_url', 'pic2_url', 'pic3_url', 'download_url1',
                  'download_url2', 'download_url3', 'download_url4', 'download_url5',
                  'downloaded_count', 'likes', 'dislikes']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'short_name','description']