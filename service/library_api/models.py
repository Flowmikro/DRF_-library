import uuid
from django.db import models


class AuthorModel(models.Model):
    """Поля автора"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author_name = models.CharField('Имя', help_text='Введите имя', max_length=60)
    author_surname = models.CharField('Фамилия', max_length=70, help_text='Введите фамилию', unique=True)

    class Meta:
        verbose_name = 'Авторы'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f'{self.author_name} {self.author_surname},  id: {self.id}'


class GenreModel(models.Model):
    """Поля жанра"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    genre_name = models.CharField('Название жанра', help_text='Введите название', max_length=30, unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return f'{self.genre_name},  id: {self.id}'


class BookModel(models.Model):
    """Поля книги"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book_name = models.CharField('Книга', help_text='Введите название книги', max_length=50, unique=True, db_index=True)
    description = models.TextField('Описание', help_text='Описание книги')
    price = models.PositiveIntegerField('Цена', help_text='Установите цену', default=100, db_index=True)
    author = models.ManyToManyField(AuthorModel, verbose_name='Автор книги', db_index=True)
    genre = models.ManyToManyField(GenreModel, verbose_name='Жанр', db_index=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'Название книги: {self.book_name}, id: {self.id}'
