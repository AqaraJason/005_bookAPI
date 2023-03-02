from django.urls import path,include
from .views import BooksAPI, BookAPI

urlpatterns = [
    path('books/', BooksAPI.as_view()),
    path('book/<int:bid>/', BookAPI.as_view())
]