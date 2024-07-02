from django.shortcuts import get_object_or_404,render
from django.http import Http404
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return HttpResponse("Hello, Customers. You're at the customer app page.")