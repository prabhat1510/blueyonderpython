from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response
from .models import Data,Customer
from .serializer import DataSerializer,CustomerSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello, Customers. You're at the customer app page.")
    
   

# Create your views here.
@api_view(['GET'])
def getData(request):
    app = Data.objects.all()
    serializer = DataSerializer(app,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
# Create your views here.
@api_view(['GET'])
def getCustomers(request):
    app = Customer.objects.all()
    serializer = CustomerSerializer(app,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postCustomer(request):
    print(request.data)
    serializer = CustomerSerializer(data=request.data)
    print("Before serializer")
    if serializer.is_valid():
        print("Inside serializer")
        serializer.save()
    return Response(serializer.data)