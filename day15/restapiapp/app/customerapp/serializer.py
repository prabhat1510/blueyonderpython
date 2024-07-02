from rest_framework import serializers
from .models import Data,Customer

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Data
        fields=('name','description')
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=('cname','dob','email','city')