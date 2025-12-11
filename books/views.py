from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

def home(request):
    books = Book.objects.all().order_by("title")
    return render(request, "books/home.html", {"books": books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "books/book_detail.html", {"book": book})


@login_required
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        year = request.POST.get("year")
        rating = request.POST.get("rating")
        description = request.POST.get("description")

        if not title or not author or not year or not rating or not description:
            return render(
                request,
                "books/book_form.html",
                {
                    "form_mode": "add",
                    "error": "All fields are required.",
                },
            )

        Book.objects.create(
            title=title,
            author=author,
            year=int(year),
            rating=float(rating),
            description=description,
            user=request.user,  # attach logged in user
        )

        return redirect("home")

    return render(request, "books/book_form.html", {"form_mode": "add"})


@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # restrict editing — only the user who added it
    if request.user != book.user:
        return redirect("home")

    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        year = request.POST.get("year")
        rating = request.POST.get("rating")
        description = request.POST.get("description")

        if not title or not author or not year or not rating or not description:
            return render(
                request,
                "books/book_form.html",
                {
                    "form_mode": "edit",
                    "book": book,
                    "error": "All fields are required.",
                },
            )

        book.title = title
        book.author = author
        book.year = int(year)
        book.rating = float(rating)
        book.description = description
        book.save()

        return redirect("books/book_detail", book_id=book.id)

    return render(request, "books/book_form.html", {"form_mode": "edit", "book": book})


@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # restrict deletion
    if request.user != book.user:
        return redirect("home")

    if request.method == "POST":
        book.delete()
        return redirect("home")

    return render(request, "books/book_confirm_delete.html", {"book": book})

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("home")

