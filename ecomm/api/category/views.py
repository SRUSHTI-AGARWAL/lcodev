from rest_framework import viewsets
from .serializers import CategorySerializer   # to JSONify the views as well.
from .models import Category

# from django.shortcuts import render    # this statement is not used as we are using django REST framework
# and not default django template
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')

# queryset determines, what is the data we are bringing from DB and based on the serializer we have written, that data will be converted
# to JSON
    serializer_class = CategorySerializer

