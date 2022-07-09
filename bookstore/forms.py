from django import forms
from bookstore.models import Books, Comments


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'released_year', 'description', 'book_cover', 'author']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['book', 'body']
