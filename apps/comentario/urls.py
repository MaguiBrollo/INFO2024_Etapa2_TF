from django.urls import path
from .views import DetallePublicacionView, EditarComentarioView, EliminarComentarioView


app_name = 'comentario'
urlpatterns = [
    path('publicacion/<int:pk>/',DetallePublicacionView.as_view(), name='detalle_publicacion'),
    path('comentario/editar/<int:pk>/', EditarComentarioView.as_view(), name='editar_comentario'),
    path('comentario/eliminar_comentario/<int:pk>/', EliminarComentarioView.as_view(), name='eliminar_comentario'),
    ]