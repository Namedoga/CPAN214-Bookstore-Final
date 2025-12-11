from rest_framework.response import Response
from rest_framework.decorators import api_view
from books.models import Book
from .serializers import BookSerializer

@api_view(["GET"])
def getBooks(request):
    books = Book.objects.all().order_by("title")
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getBook(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=404)
    
    serializer = BookSerializer(book)
    return Response(serializer.data)