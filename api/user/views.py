from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout
import re    # used for running regular expression

# generating token for user sign-in, sign-out.
# django does not generate session token of its own and has a different authentication logic.
# As long as session is active in DB , user is considered to be logged in and as the user hits the route sign-out, we will delete this token and the user is signed-out.
#
#
#
import random

def generate_session_token(length=10):
    return "".join(random.SystemRandom().choice([chr(i) for i in range(97,123)]+ [str(i) for i in range(1,10)]) for _ in range(10))
# --------------------------------------------------------------------------------------------------------------------
@csrf_exempt       # used as we will be doing sign-up from other origin request.
def sign_in(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'Send a post request with valid parameter only'})

    username= request.POST['email']
    password= request.POST['password']

# validation part
    if not re.match("^([\w\.\-_]+)?\w+@[\w-_]+(\.\w+){1,}$",username):
        return JsonResponse({'error':"Enter a valid mail"})

    if password.len() < 5:
        return JsonResponse({'error':'Password need to be alteast of 5 Characters '})

# Grabbing user model using get_user_model and thru this we will try to grab the user from DB and match its password and other stuff.

    UserModel= get_user_model()

    try:
        user= UserModel.objects.get(email= username)

        if user.check_password(password):
            usr_dict= UserModel.objects.filter(email=username).values()
            usr_dict.pop('password')  # password is popped-off here as we do not want password to go further to front-end.

    # Next we will check if there is any session token for this user or not, if it is there that means user is already logged in

            if user.session_token != 0:
                user.session_token=0
                user.save()
                return JsonResponse({'error': 'Previous Session exists'})

                token =generate_session_token()
                user.session_token= token
                user.save()
                login(request,user)
                return JsonResponse({'token':token,'user':usr_dict})
        else:
            return JsonResponse({'error': "Invalid Password"})


    except UserModel.DoesNotExist:
        return JsonResponse({'error':"Invalid Email"})

# ----------------------------------------------------------------------------------------------------------------
def signout(request,id):

#todo check for logout() placements at different places.

    UserModel = get_user_model()
# todo here

    try:
        user= UserModel.objects.get(pk=id)
        user.session_token='0'
    except UserModel.DoesNotExist():
        return JsonResponse({'error':'Invalid user ID'})
# todo here
    logout(request)
    return JsonResponse({'success': 'Logout Success'})


# Writing Viewsets
class UserViewset(viewsets.ModelViewSet):
    permission_classes_by_action = {'create':[AllowAny] }    # here we are creating object so if someone creates an account or have the create, then give them a list of Allowany
    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer

    # To get the permissions we define a method
    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]