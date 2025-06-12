from django.contrib import admin

# Register your models here.

from .models import Game, Category, Comment

admin.site.site_header = "BGames Админка"

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year', 'short_description', 'version')
    search_fields = ('name', 'short_description', 'version')
    ordering = ('id', 'name', 'year', 'short_description', 'version')
    filter_horizontal = ('categories', 'comments')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_name')
    search_fields = ('name', 'short_name', 'id')
    ordering = ('id', 'name', 'short_name')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'on_moderation')
    search_fields = ('name', 'text', 'id', 'on_moderation')
    ordering = ('id', 'name', 'text', 'on_moderation')
