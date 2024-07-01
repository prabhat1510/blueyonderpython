from django.urls import path
from . import views
from django.views.generic import TemplateView
app_name="bookapp"
urlpatterns = [
    #path('', views.index,name="index"),
    path("", views.IndexView.as_view(), name="index"),
    path("bookform/", views.displayBookForm, name="bookform"),    
    
    #path("<int:pk>/", views.DetailView.as_view(), name="detail"),   
    # ex: /bookapp/5/
    path("<int:book_id>/", views.getBookById, name="getBookById"),
    # ex: /bookapp/allBooks
    #path("allBooks/", views.allBooks, name="allBooks"),
    path("addBook/", views.addBook, name="addBook"),
    path("login/",views.login,name="login"),
    path ("loginform/",TemplateView.as_view(template_name='bookapp/login.html')),
    path("register/",views.register,name="register"),
    path ("registerform/",TemplateView.as_view(template_name='bookapp/register.html'))
    
    
  
]
