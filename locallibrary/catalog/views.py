from django.shortcuts import render, get_object_or_404
from .models import BookInstance, Book, Author, Genre
from django.views import generic

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    template_name = 'book_list.html'
    model = Book
    context_object_name = 'book_list'
    queryset = Book.objects.filter(title__icontains='war')
    paginate_by = 10

def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', context={'book': book})

def author_detail_view(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'author_detail.html', context={'author_detail': author})

class AuthorListView(generic.ListView):
    template_name = 'author_list.html'
    model = Author
    context_object_name = 'author_list'
    queryset = Author.objects.order_by('first_name')

