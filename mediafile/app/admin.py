from django.contrib import admin

# Register your models here.
from app.models import Book, Author, Category

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)
