from django.urls import path
from . import views

urlpatterns = [
    path("getBooks/", views.getBooks, name="getBooks"),
    path("getBook/<int:book_id>/", views.getBook, name="getBook"),
]