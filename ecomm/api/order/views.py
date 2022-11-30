from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model

from .serializers import OrderSerializer
from .models import Order

from django.views.decorators.csrf import csrf_exempt   #as request will be made from anotehr resource so importing csrf exempt

# Create your views here.
# for the views here first we will be validating the user i.e if user is signed in or not as Purchase will be
# allowed only for user's

# signed in
def validate_user_session(id, token):
    UserModel= get_user_model()
    try:
        user= UserModel.objects.get(pk=id)    # this one is giving us access to token so we are grabbing here token. 'user' is holding everything of 'id' given.
        if user.session_token == token:    #session_token property as seen in admin panel is equal to token that we are bringing up in request.
            return True     # true means authenticated.
        return False             # otherwise False

    except UserModel.DoesNotExist:
        return False


# whatever user is sending in admin panel we will be just adding it to the admin panel.
#  when user hits a certain  route we need to execute a method which  collects all the data and pushes that data in the admin


@csrf_exempt
def add(request,id,token):
    if not validate_user_session(id,token):
        return JsonResponse({"error":"Please login again", "code":"1"})

    if request.method== "POST":
        user_id = id
        transaction_id = request.POST["transaction_id"]
        amount = request.POST["amount"]

        products = request.POST["products"]
        total_pro = len(products.split(',')[:-1])

        UserModel= get_user_model()
        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return JsonResponse({"error": "User does not exist"})

        ordr=Order(user=user, product_names= products,total_products=total_pro,transaction_id=transaction_id)
        ordr.save()
        return JsonResponse({'success': True, 'error': False, 'msg': 'Order Placed successfully'})


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('user')
    serializer_class = OrderSerializer
