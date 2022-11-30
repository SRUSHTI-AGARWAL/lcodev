from django.urls import path,include
from .views import home
from rest_framework.authtoken import views
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here SimpleisbetterthanComplex

urlpatterns = [

    # todo Adding urls for django REST framework

    path('',home,name='api.home'),
# this home route is / and it can also be represented by '' (empty)
#     path('',views.home, name='home'),
    #
    #  this path will be given if api.home path is not given
    # todo adding path for api also. Though only api can handle the request but we will be creating api.urls to
    #  provide access to handle further url requests so creating api.urls file
    # Adding urls to other Django Apps

    path('category/', include('api.category.urls')),     # this route is /category
    path('product/', include('api.product.urls')),
    path('user/', include('api.user.urls')),
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
    path('order/', include('api.order.urls')),
    path('payment/', include('api.payment.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here SimpleisbetterthanComplex


]