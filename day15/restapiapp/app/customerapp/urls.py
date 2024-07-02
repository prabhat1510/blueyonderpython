from django.urls import path
from . import views
from django.views.generic import TemplateView
app_name="bookapp"
urlpatterns = [
    path('', views.index,name="index"),
    #path("", views.IndexView.as_view(), name="index"),
]