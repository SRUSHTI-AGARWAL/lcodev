from django.db import models
from api.category.models import Category
# Create your models here.

class Product(models.Model):
    price= models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    stock = models.CharField(max_length= 50)
    description = models.CharField(max_length=250)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    is_active= models.BooleanField(default= True, blank= True)
    image =  models.ImageField(upload_to='images/', blank= True, null= True)
    category = models.ForeignKey(Category, on_delete= models.SET_NULL, blank=True,null= True )
    # interlinking tables in category field using Foreign key.
    #  If blank= true is there, then only null = True can be there.


    def __str__(self):
        return self.name




