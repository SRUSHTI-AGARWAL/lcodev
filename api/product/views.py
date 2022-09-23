# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product
# Create your views here.

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')  #name or id anything can be used.
    serializer_class = ProductSerializer

    # what is the query that we want to fire and how we would like to serialize it i.e what i sthe class that would be serializing it.


