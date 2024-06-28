from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_price = models.IntegerField(default=0)
    book_publisher=models.CharField(max_length=100)
    pub_date = models.DateTimeField("date published")
    

