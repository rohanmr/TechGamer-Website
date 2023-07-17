"""myblog URL Configuration

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
from os import name
from django.contrib import admin
from django.urls import path,include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('latest1/',views.latest1,name='latest1'),
    path('latest2/',views.latest2,name='latest2'),
    path('latest3/',views.latest3,name='latest3'),
    path('data/',views.data,name='data'),
    path('data1/',views.data1,name='data1'),
    path('all/',views.all,name='all'),
    path ('searched/',views.search,name="searched"),
    path('',include('post.urls'))
]

