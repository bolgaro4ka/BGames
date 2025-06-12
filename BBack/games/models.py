from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=255)
    short_name = models.CharField(verbose_name='Краткое имя', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Comment(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=255)
    text = models.TextField(verbose_name='Текст', max_length=2048)

    on_moderation = models.BooleanField(verbose_name='На модерации', default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class Game(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=255)

    categories = models.ManyToManyField(Category, verbose_name="Категории")
    comments = models.ManyToManyField(Comment, verbose_name="Комментарии")

    image_url = models.CharField(verbose_name="URL картинки", max_length=255)
    game_url = models.CharField(verbose_name="URL игры", max_length=255)

    short_description = models.TextField(verbose_name="Описание", default="")

    long_description = models.TextField(verbose_name="Полное описание", default="")

    year = models.IntegerField(verbose_name="Год", default=0)
    developer = models.CharField(verbose_name="Разработчик", max_length=255, default="")
    version = models.CharField(verbose_name="Версия", max_length=255, default="")
    language = models.CharField(verbose_name="Язык", max_length=255, default="")
    tablet = models.CharField(verbose_name="Таблетка", max_length=255, default="")
    genre = models.CharField(verbose_name="Жанр", max_length=255, default="")

    os = models.CharField(verbose_name="Операционная система", max_length=255, default="")
    cpu = models.CharField(verbose_name="Процессор", max_length=255, default="")
    ram = models.CharField(verbose_name="Оперативная память", max_length=255, default="")
    gpu = models.CharField(verbose_name="Видео карты", max_length=255, default="")
    size = models.CharField(verbose_name="Размер", max_length=255, default="")

    additional_info = models.TextField(verbose_name="Дополнительная информация", default="")

    pic1_url = models.CharField(verbose_name="URL картинки 1", max_length=255, default="")
    pic2_url = models.CharField(verbose_name="URL картинки 2", max_length=255, default="")
    pic3_url = models.CharField(verbose_name="URL картинки 3", max_length=255, default="")
    
    download_url1 = models.CharField(verbose_name="Ссылка на скачивание 1", max_length=255, default="")
    download_url2 = models.CharField(verbose_name="Ссылка на скачивание 2", max_length=255, default="")
    download_url3 = models.CharField(verbose_name="Ссылка на скачивание 3", max_length=255, default="")
    download_url4 = models.CharField(verbose_name="Ссылка на скачивание 4", max_length=255, default="")
    download_url5 = models.CharField(verbose_name="Ссылка на скачивание 5", max_length=255, default="")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
