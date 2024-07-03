from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework import status
from .models import Data,Customer
from .serializer import DataSerializer,CustomerSerializer
from .exceptions import CustomerNotFoundException


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
    print(serializer.data)
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

@api_view(['GET'])    
def getCustomerById(request,id):
    #custID = request.query_params.get("id", None)
    customer = Customer.objects.filter(pk=id)
    serializer = CustomerSerializer(customer,many=True)
    print(serializer.data)
    return Response(serializer.data)
    
@api_view(['GET'])    
def getCustomerByName(request,cname):
    #custID = request.query_params.get("id", None)
    try:
        customer = Customer.objects.filter(cname=cname)
        print(customer)
        if not customer:
            raise CustomerNotFoundException
        else:
            serializer = CustomerSerializer(customer,many=True)
            return Response(serializer.data)
    except CustomerNotFoundException:
           return Response("Cusomter with customer name "+cname+" not found")


@api_view(['GET'])    
def getCustomerByNameUsingReqParams(request):
    cname = request.query_params.get("cname", None)
    try:
        customer = Customer.objects.filter(cname=cname)
        print(customer)
        if not customer:
            raise CustomerNotFoundException
        else:
            serializer = CustomerSerializer(customer,many=True)
            return Response(serializer.data)
    except CustomerNotFoundException:
           return Response("Cusomter with customer name "+cname+" not found") 
 
@api_view(['DELETE'])    
def deleteCustomerById(request):
    try:
        cid = request.query_params.get("id", None)
        customer = Customer.objects.get(pk=cid)
        if not customer:
            raise CustomerNotFoundException
        else:
            customer.delete()
            return Response({'msg': 'Person deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except CustomerNotFoundException:
           return Response("Cusomter with customer id not found")