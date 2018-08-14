from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('books/', BookListView.as_view(), name='books'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('book/<uuid:pk>/renew/', renew_book_librarian, name='renew-book-librarian'),
    path('author/create/', AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', AuthorDelete.as_view(), name='author_delete'),
]
