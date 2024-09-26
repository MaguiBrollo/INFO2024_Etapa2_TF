"""
URL configuration for proyBlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from .views import index, NosotrosView,ContactanosView, BlogView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('nosotros/',NosotrosView.as_view(),name="nosotros"),
    path('blog/', BlogView.as_view(),name="blog"),
    path('contactanos/',ContactanosView.as_view(),name="contactanos"),

   # path('', IndexView.as_view(), name='index'),
   # path('', AboutView.as_view(), name='about'),
]

