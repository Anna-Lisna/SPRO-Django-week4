from django.urls import path
from .views import BookDetailView, ShowAuthor, ShowBooks, add_book, add_comment

urlpatterns = [
    path('books', ShowBooks.as_view(), name='book_list'),
    path('books/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('books/comment', add_comment, name='comment'),
    path('author/<int:pk>', ShowAuthor.as_view(), name='author'),
    path('form', add_book, name='form')
]
