from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/%d-%m-%y')


class Author(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='authors/%d-%m-%y')
    biography = models.TextField()


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='books/%d-%m-%y')
    description = models.TextField()
    category = models.ForeignKey(Category,
                                 related_name='categories',
                                 on_delete=models.CASCADE)
    author = models.ForeignKey(Author,
                               related_name='authors',
                               on_delete=models.CASCADE)
