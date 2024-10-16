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
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import NosotrosView,BlogView
from .viewsC import contactanosView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('nosotros/',NosotrosView.as_view(),name="nosotros"),
    path('blog/', BlogView.as_view(),name="blog"),
    path('contactanos/',contactanosView,name="contactanos"),

    path('usuarios/', include('apps.usuarios.urls')),

    path("usuarios/", include("django.contrib.auth.urls")),
]
# LEER LAS URL DE LAS IMAGENES
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#no tengo STATIC en las apps
#urlpatterns += staticfiles_urlpatterns()