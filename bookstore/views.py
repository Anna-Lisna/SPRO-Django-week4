from django.shortcuts import render, redirect
from django.views.generic import ListView
from bookstore.forms import BookForm, CommentForm
from bookstore.models import Books, Authors, Comments
from django.views.generic.base import View


class ShowBooks(View):
    def get(self, request):
        books = Books.objects.all().order_by('-id')
        if request.method == "GET" and "search" in request.GET:
            search = request.GET['search']
            books = books.filter(title__contains=search)
        return render(request, 'bookstore/book_list.html', context={'books': books})


def add_book(request):
    form = BookForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'bookstore/form.html', context={'book_form': BookForm})


class BookDetailView(ListView):
    model = Books
    template_name = 'bookstore/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['pk']
        context['book'] = Books.objects.get(id=id)
        context['comments'] = Comments.objects.filter(book_id__exact=id)
        return context


class ShowAuthor(ListView):
    model = Authors
    template_name = 'bookstore/author.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['pk']
        context['author'] = Authors.objects.get(id=id)
        context['books'] = Books.objects.filter(author_id__exact=id)
        return context


def add_comment(request):
    form = CommentForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        book = data['book']
        body = data['body']
        author = request.user
        Comments.objects.create(book=book, body=body, author=author)
        return redirect('book_detail', pk=book.id)
    return render(request, 'bookstore/comment.html', context={'comment_form': CommentForm})


