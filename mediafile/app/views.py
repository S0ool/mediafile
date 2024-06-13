from django.shortcuts import render, redirect

# Create your views here.
from app.models import Book, Author, Category


def index(request):
    ctx = {
        'books': Book.objects.all(),
        'authors': Author.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'app/index.html', context=ctx)


def books(request):
    ctx = {
        'books': Book.objects.all(),
        'authors': Author.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'app/books.html', context=ctx)


def categories(request):
    ctx = {
        'categories': Category.objects.all()
    }
    return render(request, 'app/categories.html', context=ctx)


def authors(request):
    ctx = {
        'authors': Author.objects.all(),
    }
    return render(request, 'app/authors.html', context=ctx)


def create_book(request):
    if request.method == "POST":
        book = Book()
        if request.POST.get('book_name') == '' or request.FILES.get('book_image') == '':
            return redirect('books')
        book.name = request.POST.get('book_name')
        book.image = request.FILES.get('book_image')
        book.description = request.POST.get('book_description')
        book.author = Author.objects.get(id=request.POST.get('author_id'))
        book.category = Category.objects.get(id=request.POST.get('category_id'))
        book.save()
    return redirect('books')


def change_book(request):
    if request.method == "POST":
        book = Book.objects.get(id=request.POST.get('book_id'))
        if request.POST.get('book_name') == '' or request.FILES.get('book_image') == '':
            return redirect('books')
        book.name = request.POST.get('book_name')
        book.image = request.FILES.get('book_image')
        book.description = request.POST.get('book_description')
        book.author = Author.objects.get(id=request.POST.get('author_id'))
        book.category = Category.objects.get(id=request.POST.get('category_id'))
        book.save()
    return redirect('books')


def delete_book(request):
    book = Book.objects.get(id=request.POST.get('book_id'))
    book.delete()
    return redirect('books')


def create_category(request):
    if request.method == "POST":
        category = Category()
        if request.POST.get('category_name') == '' or request.FILES.get('category_image') == '':
            return redirect('categories')
        category.name = request.POST.get('category_name')
        category.image = request.FILES.get('category_image')
        category.save()
    return redirect('categories')


def change_category(request):
    if request.method == "POST":
        category = Category.objects.get(id=request.POST.get('category_id'))
        if request.POST.get('category_name') == '' or request.FILES.get('category_image') == '':
            return redirect('categories')
        category.name = request.POST.get('category_name')
        category.image = request.FILES.get('category_image')
        category.save()
    return redirect('categories')


def delete_category(request):
    category = Category.objects.get(id=request.POST.get('category_id'))
    category.delete()
    return redirect('categories')


def create_author(request):
    if request.method == "POST":
        author = Author()
        if request.POST.get('author_name') == '' or request.FILES.get('author_image') == '':
            return redirect('authors')
        author.name = request.POST.get('author_name')
        author.image = request.FILES.get('author_image')
        author.save()
    return redirect('authors')


def change_author(request):
    if request.method == "POST":
        author = Author.objects.get(id=request.POST.get('author_id'))
        if request.POST.get('author_name') == '' or request.FILES.get('author_image') == '':
            return redirect('authors')
        author.name = request.POST.get('author_name')
        author.image = request.FILES.get('author_image')
        author.save()
    return redirect('authors')


def delete_author(request):
    author = Author.objects.get(id=request.POST.get('author_id'))
    author.delete()
    return redirect('authors')


def category(request, category_id):
    category = Category.objects.get(id=category_id)
    ctx = {
        'category': category,
        'books': Book.objects.filter(category=category)
    }
    return render(request, 'app/category.html', context=ctx)
