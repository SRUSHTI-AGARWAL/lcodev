from django.urls import include,path
from . import views
# from rest_framework import routers


urlpatterns = [

    path('gettoken/<str:id>/<str:token>', views.generate_token,name="token.generate"),
    path('process/<str:id>/<str:token>', views.process_payment,name="payment.process"),

]