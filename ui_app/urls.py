from django.urls import path
from .views import register_view, login_view, logout_view, home_view, add_book, book_detail, search_books

urlpatterns = [
    path('', home_view, name='home'),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("add_book/", add_book, name="add_book"),
    path('book/<int:id>/', book_detail, name='book_detail'),
    path('search/', search_books, name='search_books'),
]
