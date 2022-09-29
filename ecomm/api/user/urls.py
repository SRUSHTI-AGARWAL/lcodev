from django.urls import path,include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'', views.UserViewset)

# path is left empty as this has already been taken care-of by urls in api.urls as per api/category
#  though urls= router.urls can be used but we will be using the similar way we have been using for urls.

urlpatterns = [

    path('login/',views.sign_in,name='sign_in'),
    path('logout/<int:id>/',views.signout,name='signout'),  # <>defines a capture group.
    path('',include(router.urls))
    ]



# The ** operator allowsyou to ake a dictionary of key-value pairs and unpack it into keyword arguments in a fucntion call.
# functions in python cannot have the same keyworeded arguments.