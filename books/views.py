from django.shortcuts import render, get_object_or_404, redirect

def home(request):
    books = []  
    return render(request, 'books/home.html', {'books': books})


def book_detail(request, book_id):
    return render(request, 'books/book_detail.html', {'book_id': book_id})


def add_book(request):
    return render(request, 'books/book_form.html', {'form_mode': 'add'})


def edit_book(request, book_id):
    return render(request, 'books/book_form.html', {'form_mode': 'edit', 'book_id': book_id})


def delete_book(request, book_id):
    return render(request, 'books/book_confirm_delete.html', {'book_id': book_id})
