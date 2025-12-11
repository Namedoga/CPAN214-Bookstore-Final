from django.shortcuts import render, get_object_or_404, redirect
from .models import Book


def home(request):
    books = Book.objects.all().order_by("title")
    return render(request, "books/home.html", {"books": books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "books/book_detail.html", {"book": book})


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
        )
        return redirect("home")

    

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

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
        return redirect("book_detail", book_id=book.id)

    
    return render(
        request,
        "books/book_form.html",
        {
            "form_mode": "edit",
            "book": book,
        },
    )


def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.delete()
        return redirect("home")

    return render(request, "books/book_confirm_delete.html", {"book": book})

