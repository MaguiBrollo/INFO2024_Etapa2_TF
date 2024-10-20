from django.urls import path
from .views import CrearPublicacionView, DetallePublicacionView,  EditarPublicacionView,  ListaPublicacionesView, BorrarPublicacionView
from .views import EditarCategoriaView, EliminarCategoriaView, ListaCategoriasView, ListaPublicacionesPorCategoriaView, CrearCategoriaView

urlpatterns = [
    path('crear/', CrearPublicacionView.as_view(), name='crear_publicacion'),
    path('lista/', ListaPublicacionesView.as_view(), name='lista_publicaciones'),
    path('publicacion/<int:pk>/', DetallePublicacionView.as_view(), name='detalle_publicacion'), 
    path('publicacion/<int:pk>/editar/', EditarPublicacionView.as_view(), name='editar_publicacion'),
    path('publicacion/<int:pk>/eliminar/', BorrarPublicacionView.as_view(), name='eliminar_publicacion'),
    path('publicaciones/categoria/<int:categoria_id>/', ListaPublicacionesPorCategoriaView.as_view(), name='lista_publicaciones_categoria'),
    path('categoria/nueva/', CrearCategoriaView.as_view(), name='crear_categoria'),
    path('categorias/', ListaCategoriasView.as_view(), name='lista_categorias'),
    path('categoria/editar/<int:pk>/', EditarCategoriaView.as_view(), name='editar_categoria'),
    path('categoria/eliminar/<int:pk>/', EliminarCategoriaView.as_view(), name='eliminar_categoria'),
]