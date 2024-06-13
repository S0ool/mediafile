from django.contrib import admin
from django.urls import path

from app.views import index, create_book, authors, change_book, delete_book, change_category, \
    create_category, delete_category, categories, books, create_author, change_author, delete_author, category

urlpatterns = [
    path('', index, name='index'),
    path('books', books, name='books'),
    path('categories', categories, name='categories'),
    path('authors', authors, name='authors'),

    path('create_book', create_book, name='create_book'),
    path('change_book', change_book, name='change_book'),
    path('delete_book', delete_book, name='delete_book'),
    path('create_category', create_category, name='create_category'),
    path('change_category', change_category, name='change_category'),
    path('delete_category', delete_category, name='delete_category'),
    path('create_author', create_author, name='create_author'),
    path('change_author', change_author, name='change_author'),
    path('delete_author', delete_author, name='delete_author'),

    path('category/<int:category_id>', category, name='category'),

]


