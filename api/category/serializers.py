from rest_framework import serializers
from .models import Category
# from rest_framework.renderers import JSONRenderer


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Category
        fields = ('name','description')


