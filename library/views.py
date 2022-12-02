# Windows - pip install psycopg2 
# Mac -     pip3 install psycopg2-binary

from django.shortcuts import render
from .models import Book, List

book_list = {
    '1': {
        'id': '1',
        'title': 'The Way of Kings',
        'author': 'Brandon Sanderson',
        'price': 10.99,
        'image': 'https://m.media-amazon.com/images/I/51ZX3mqLFzL.jpg'
    },
    '2': {
        'id': '2',
        'title': 'The Name of the Wind',
        'author': 'Patrick Rothfuss',
        'price': 8.99,
        'image': 'https://m.media-amazon.com/images/I/51JThzjy3gL._AC_SY780_.jpg'
    },
    '3': {
        'id': '3',
        'title': 'Mistborn',
        'author': 'Brandon Sanderson',
        'price': 9.99,
        'image': 'https://m.media-amazon.com/images/I/51sKzl+R6OL._AC_SY780_.jpg'
    }
}

# Create your views here.
def indexPageView(request):
    db_books = Book.objects.all()

    # for book in db_books:
    #     print(book.author.contact_info.email)

    context = {
        "books": db_books
    }

    return render(request, 'library/index.html', context)

def aboutPageView(request):
    return render(request, "library/about.html")

def bookPageView(request, book_id):
    # Find a book from the book id
    # SQL - SELECT * FROM books WHERE id=book_id
    book = Book.objects.get(id=book_id)
    print("book", book)

    # Create a context dictionary
    context = {
        "book": book
    }

    # Render out an html template
    return render(request, "library/book.html", context)

def listsPageView(request):
    lists = List.objects.all()

    for list in lists:
        print("BOOKS", list.books.all())

    context = {
        'lists': lists
    }

    return render(request, "library/lists.html", context)
