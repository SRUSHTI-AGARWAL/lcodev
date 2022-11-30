from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

import braintree
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

gateway = braintree.BraintreeGateway(
  braintree.Configuration(
    environment=braintree.Environment.Sandbox,
    merchant_id='7qsbsbbwqc325gc9',
    public_key='fm6vkh5gv7tpp8ww',
    private_key='4ef808611b969bd0b4f7c13adb022e0a'
  )
)
# ------------------------------------------------------------------------------------------
# before sending the token back to client, we will check if the user is signed-in then only user is validated to make a purchase

def validate_user_session(id,token):
    UserModel= get_user_model()
    try:
        user=UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        else:
            return False
    except UserModel.DoesNotExist:
        return JsonResponse({"error":" Please login first"})

# ------------------------------generating  client token----------------------------------------------------------------------
@csrf_exempt    #adding this as request will be made from react frontend

def generate_token(request, token,id):  #user will send a request and we will verify it using id and token
    if not validate_user_session(id,token):
        return JsonResponse({"error":"Invalid Session, Please login first! "})

    return JsonResponse({"client_token":gateway.client_token.generate(),"success":True })

# ----------------------------------------------------------------------------------------
@csrf_exempt
def process_payment(request,id,token):
    # again we will validate a session
    if not validate_user_session(id,token):
        return JsonResponse({"error":"Invalid Session, Please login first! "})

    nonce_from_the_client = request.form["paymentMethodNonce"]
    amount_from_the_client = request.form["amount"]

    result = gateway.transaction.sale({
        "amount": amount_from_the_client,
        "paymentMethodNonce": nonce_from_the_client,
        "options": {
            "submit_for_settlement": True
        }
    })
    print(result)
    if result.is_success:
        return JsonResponse({"success":"result.is success",
                             "transaction":{"id":result.transaction.id,"amount":result.transaction.amount}
                             })
    else:
        return JsonResponse({"error":True,"success":False})
    # transaction will be an object.