from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Books


@login_required
def index(request):
    books = Books.objects.all()

    return render(request, 'index.html', {'books': books, 'title': 'Home'})


def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'index.html')
    context['form'] = form
    return render(request, 'sign_up.html', context)


@login_required
def add_book(request):
    form = BookForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        book = Books.objects.create(
            book_name=form.data['book_name'],
            author=form.data['author'],
            publish_date=form.data['publish_date'],
            desc=form.data['desc'],
            img=request.FILES['img']
        )
        book.save()
        return redirect('/')

    return render(request, 'add_book.html', {'form': form, 'title': 'Add Book'})


@login_required
def edit_book(request, pk):
    item = Books.objects.get(pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm(instance=item)
        return render(request, 'edit_book.html', {'form': form, 'title': 'Edit Book'})


@login_required()
def delete_book(request, pk):
    item = Books.objects.get(pk=pk)
    item.delete()
    return redirect('/')

