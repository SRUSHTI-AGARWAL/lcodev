"""ecomm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),     # urls for handling admin panel

    #todo Adding urls for django REST framework
    path('api-auth/',include('rest_framework.urls')),
    # path(r'^api-auth/', include('rest_framework.urls')),

    # adding path for api also. Though only api can handle the request but we will be creating api.urls to provide
    # access to handle further url requests so creating api.urls file.
    
    path('api/',include('api.urls')),    #url for handling api app
]
# this is the general syntax and includes boilerplate code.

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# mentioning link(url) for media so it is accessible.Just another URL pattern