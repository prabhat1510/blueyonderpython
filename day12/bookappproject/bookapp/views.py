from django.utils import timezone
from django.shortcuts import get_object_or_404,render
from django.http import Http404
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.views import generic
from bookapp.models import Book
import json

def index(request):
    return HttpResponse("Hello, I am you book app.")

'''
def getBookById(request, book_id):
    response = Book.objects.get(id=book_id)
    return HttpResponse(response)


def allBooks(request):
    response = Book.objects.all()
    return HttpResponse(response)

def addBook(request):
        data = json.loads(request.body)
        b= Book(book_name =data.get('book_name') ,book_author =data.get('book_author') ,book_price = data.get('book_price'),book_publisher=data.get('book_publisher'),pub_date=timezone.now())
        # Save the object into the database. You have to call save() explicitly.
        b.save()
        return HttpResponse(b.id)
'''
class IndexView(generic.ListView):
    template_name = "bookapp/index.html"
    context_object_name = "book_list"

    def get_queryset(self):
        """Return the last five books."""
        return Book.objects.order_by("book_price")[:5]

'''
class DetailView(generic.DetailView):
    #model = Book
    template_name = "bookapp/detail.html"
    context_object_name = "book"
    def get_queryset(self):
        return Book.objects.get(pk=id)
'''
def getBookById(request, book_id):
    #response = Book.objects.get(id=book_id)
    #return HttpResponse(response)
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "bookapp/detail.html", {"book": book})