from rest_framework import serializers
from .models import Category
# from rest_framework.renderers import JSONRenderer




class CategorySerializer(serializers.Serializer):
    class Meta:
        model=  Category
        field= ('name','description')


