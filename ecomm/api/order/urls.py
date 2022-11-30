from django.urls import path,include
from . import views
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'', views.OrderViewSet)
# path is left empty as this has already been taken care-of by urls in api.urls as per api/category

#  though urls= router.urls can be used but we will be using the similar way we have been using for urls.

urlpatterns = [
    path('add/<str:id>/<str:token>/',views.add,name='order.add'),
    path('', include(router.urls)),

]
