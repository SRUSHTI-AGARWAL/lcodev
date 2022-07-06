from django.urls import path,include
from .views import home
from rest_framework.authtoken import views



urlpatterns = [

    # todo Adding urls for django REST framework

    # path('api-auth/', include('rest_framework.urls')),
    path('',home,name='api.home'),

    # todo adding path for api also. Though only api can handle the request but we will be creating api.urls to provide
    # access to handle further url requests so creating api.urls file
    # Adding urls to other Django Apps

    path('category/', include('api.category.urls')),

    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth')

    # path('order/', include('api.order.urls')),
    # path('payment/', include('api.payment.urls')),
    # path('product/', include('api.product.urls')),
    # path('user/', include('api.user.urls'))
]