from rest_framework import serializers
from .models import Data,Customer

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Data
        fields=('name','description')
        
class CustomerSerializer(serializers.ModelSerializer):
    #dob=serializers.DateField(format="%Y-%m-%d",input_formats="%Y-%m-%d")
    class Meta:
        
        model=Customer
        fields=('cname','dob','email','city')