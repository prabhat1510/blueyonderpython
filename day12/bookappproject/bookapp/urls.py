from django.urls import path
from . import views
app_name="bookapp"
urlpatterns = [
    #path('', views.index,name="index"),
    path("", views.IndexView.as_view(), name="index"),  
    #path("<int:pk>/", views.DetailView.as_view(), name="detail"),   
    # ex: /bookapp/5/
    path("<int:book_id>/", views.getBookById, name="getBookById"),
    # ex: /bookapp/allBooks
    #path("allBooks/", views.allBooks, name="allBooks"),
     #path("addBook/", views.addBook, name="addBook"),
  
]
