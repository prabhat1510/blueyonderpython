from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_price = models.IntegerField(default=0)
    book_publisher=models.CharField(max_length=100)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.book_name+"  "+self.book_author+"  "+str(self.book_price)+"  "+self.book_publisher+"  "+str(self.pub_date)
    

class Login(models.Model):
    username =  models.CharField(max_length =100)
    password = models.CharField(max_length =100)
 
class Register(models.Model):
    fName = models.CharField(max_length =50)
    lName = models.CharField(max_length =50)
    email = models.CharField(max_length = 50)
    username = models.CharField(max_length =30)
    password = models.CharField(max_length =100) 