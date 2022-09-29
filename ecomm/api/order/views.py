from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .serializers import OrderSerializer
from .models import Order
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# for the views here first we will be valiating the user i.e if user is signed in or not as Purchase will be allowed only for user's
# signed in
def validate_user_session(id, token):



