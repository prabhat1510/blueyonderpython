from django.utils import timezone
from django.shortcuts import get_object_or_404,render,redirect
from django.http import Http404
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.views import generic
from bookapp.models import Book,Login,Register
import json
import datetime
from django.utils import timezone
from bookapp.forms import LoginForm,RegisterForm
def index(request):
    return HttpResponse("Hello, I am you book app.")

'''
def getBookById(request, book_id):
    response = Book.objects.get(id=book_id)
    return HttpResponse(response)


def allBooks(request):
    response = Book.objects.all()
    return HttpResponse(response)
'''
def addBook(request):
        #print("************"+str(request.POST["book"]))
        #data = json.loads(request.body)
        #b= Book(book_name =data.get('book_name') ,book_author =data.get('book_author') ,book_price = data.get('book_price'),book_publisher=data.get('book_publisher'),pub_date=timezone.now())
        # Save the object into the database. You have to call save() explicitly.
        #b.save()
        global b
        if request.method == 'POST':
            bookname = request.POST["bookname"]
            bookauthor = request.POST["bookauthor"]
            bookprice = request.POST["bookprice"]
            bookpub = request.POST["bookpub"]
            b= Book(book_name =bookname,book_author=bookauthor,book_price=bookprice,book_publisher=bookpub,pub_date=timezone.now())
            print(b)
        #b=Book(book_name =request.POST["bookname"])
        b.save()
        #return  HttpResponse(b.id)
        return  redirect("bookapp:index")
        #return render(request,"bookapp/index.html",{"book":""})
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
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "bookapp/detail.html", {"book": book})
    
def displayBookForm(request):
    template_name = "bookapp/addbookform.html"
    context = {"book":""}
    return render(request, template_name, context)
    
def login(request):
   username = "not logged in"
   context ={"username" : ""}
   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)
      
      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
         password = MyLoginForm.cleaned_data['password']
         dbUser = Login.objects.filter(username=username).values()
         if(dbUser[0].get("password") == password):
            print("Logged in successfully")
            context = {"username" : username+ " Logged in successfully"}
         else:
            context = {"username" : username+" Password not matching"}
            print("Password not matching")
         print(username)
   else:
      MyLoginForm = LoginForm()
		
   return render(request, 'bookapp/loggedin.html', context)

def register(request):
    
   username = "not logged in"
   
   if request.method == "POST":
      #Get the posted form
      MyRegisterForm = RegisterForm(request.POST)
      
      if MyRegisterForm.is_valid():
         username = MyRegisterForm.cleaned_data['username']
         password = MyRegisterForm.cleaned_data['password']
         fName = MyRegisterForm.cleaned_data['fName']
         lName = MyRegisterForm.cleaned_data['lName']
         email = MyRegisterForm.cleaned_data['email']
         login = Login(username=username,password=password)
         login.save()
         reg = Register(fName=fName,lName=lName,email=email,login=login)
         reg.save()
   else:
      MyRegisterForm = RegisterForm()
   return render(request, 'bookapp/registered.html', {"username" :username})
   
def home(request):
    template_name = "bookapp/home.html"
    context = {"msg":""}
    return render(request, template_name, context)
    
def loginForm(request):
    template_name='bookapp/login.html'
    context ={"msg":""}
    return render(request, template_name, context)

def regForm(request):
    template_name='bookapp/register.html'
    context ={"msg":""}
    return render(request, template_name, context)
    