from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, BookForm
from .models import CustomUser, Book


def is_manager(user):
    return user.groups.filter(name="Менеджеры").exists()

@login_required
def home_view(request):
    books = Book.objects.all()
    return render(request, "home.html", {"books": books, "is_manager": is_manager(request.user)})

@user_passes_test(is_manager)  # Только менеджеры могут добавлять книги
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = BookForm()
    return render(request, "add_book.html", {"form": form})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'book_detail.html', {'book': book})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)  # Добавляем request.FILES
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("home")

def search_books(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(description__icontains=query)
        )

    return render(request, 'search_results.html', {'results': results, 'query': query})