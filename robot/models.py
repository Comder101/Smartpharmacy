from django.db import models

class Category(models.Model):
    # allowed= models.BooleanField(default=False)
    category= models.CharField(max_length=50, default="fruits")

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

class Product(models.Model):
    productname = models.CharField(max_length=60,default="Crocin")
    productprice= models.IntegerField(default=300)
    quantity= models.IntegerField(default=10)
    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter (id__in=ids)
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter (category=category_id)
        else:
            return Product.get_all_products()
    
class Customer(models.Model):
    firstname = models.CharField(max_length=50,default='Kartik')
    lastname = models.CharField (max_length=50,default='Singhania')
    contact = models.CharField(max_length=10)
    email=models.EmailField(max_length=50,default='karsingh@gmail.com')
    city = models.CharField(max_length=50,default='Koregaon')
    #to save the data
    def register(self):
        self.save()

from django.contrib.auth.models import User

# Create your models here.
