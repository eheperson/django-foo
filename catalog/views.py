from django.shortcuts import render
# Create your views here.

from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


from django.views import generic

class BookListView(generic.ListView):
    model = Book

    paginate_by = 10
    # With this addition, as soon as you have more than 10 records the view will start paginating the data it sends to the template. 
    # The different pages are accessed using GET parameters. 
    # to access page 2 you would use the URL :   /catalog/books/?page=2.


    # # basically 
    # context_object_name = 'book_list'   # your own name for the list as a template variable
    # queryset = Book.objects.filter()[:5] # Get 5 books containing the title war
    # template_name = 'catalog/book_list.html'  # Specify your own template name/location

    # If a requested record does not exist then the generic class-based detail view will raise an Http404 exception for you automaticall— in production, 


    # def get_queryset(self):
    #     """  
    #     we can override the get_queryset() method to change the list of records returned. 
    #     This is more flexible than just setting the 'queryset' attribute as we did in 
    #     the preceding code fragment (though there is no real benefit in this case):
    #     """
    #     return Book.objects.filter(title__icontains='man')[:5] # Get 5 books containing the title war

def get_context_data(self, **kwargs):
    """
    We might also override get_context_data() in order to pass additional context variables to the template
    """
    # Call the base implementation first to get the context
    context = super(BookListView, self).get_context_data(**kwargs)
    # Create any data and add it to the context
    # context['some_data'] = 'This is just some data'
    return context

# - - - - Bound - Begin - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class BookDetailView(generic.DetailView):
    """
    This class based view finds the book_detail.py but I am not sure how.
    I did not give any reference or path to that motherfucker book_detaii.html page.  
    """ 
    model = Book
#
#
from django.shortcuts import Http404
def book_detail_view(request, primary_key):
    """
    function based version of class BookDetailView(generic.DetailView):


    Just to give you some idea of how this works, 
    the code fragment below demonstrates how you would implement 
    the class-based view as a function if you were not using the generic class-based detail view.
    """
    try:
        book = Book.objects.get(pk=primary_key)
    except Book.DoesNotExist:
        raise Http404('Book does not exist')

    return render(request, 'catalog/book_detail.html', context={'book': book})
#
# # # Alternatively, we can use the get_object_or_404() function as 
# # # a shortcut to raise an Http404 exception if the record is not found.
#
# from django.shortcuts import get_object_or_404
# def book_detail_view(request, primary_key):
#     book = get_object_or_404(Book, pk=primary_key)
#     return render(request, 'catalog/book_detail.html', context={'book': book})
#
# - - - - Bound - End - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
