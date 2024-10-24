from django.urls import path
from .views import DetallePublicacionView


app_name = 'comentario'
urlpatterns = [
    path('publicacion/<int:pk>/', DetallePublicacionView.as_view, name='detalle_publicacion'),
    ] 