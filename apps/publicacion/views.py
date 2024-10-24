from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_list_or_404

from ProyectoFinal.proyBlog.apps.comentario.forms import ComentarioForm
from .models import Publicacion, Categoria
from django.views.generic import CreateView,ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from .forms import CategoriaForm, PublicacionForm
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.

# Clase de crear categorias

class CrearPublicacionView(UserPassesTestMixin, CreateView):
    model = Publicacion
    form_class = PublicacionForm
    template_name = 'crear_publicacion.html'
    success_url = reverse_lazy('lista_publicaciones')

    # Este método asigna el autor al usuario logeado
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


    def test_func(self):
        # Permitir a usuarios regulares, staff y superusuarios crear categorías
        return (self.request.user.is_authenticated and 
                (self.request.user.is_superuser or self.request.user.is_staff or self.request.user.is_authenticated))


# Clase para crear categorias

class CrearCategoriaView(UserPassesTestMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias/crear_categoria.html'

    def form_valid(self, form):
        form.save()
        return redirect('lista_publicaciones')

    def test_func(self):
        # Permitir a usuarios regulares, staff y superusuarios crear categorías
        return (self.request.user.is_authenticated and 
                (self.request.user.is_superuser or self.request.user.is_staff or self.request.user.is_authenticated))


# Clase para listar las publicaiones segun su categoria

class ListaPublicacionesPorCategoriaView(ListView):
    model = Publicacion
    template_name = 'lista_publicaciones.html'
    context_object_name = 'publicaciones'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context

    def get_queryset(self):
        categoria_id = self.kwargs.get('categoria_id')
        if categoria_id:
            return Publicacion.objects.filter(categoria_id=categoria_id)
        return Publicacion.objects.all()

# Clase para listar las publicaciones

class ListaPublicacionesView(ListView):
    model = Publicacion
    template_name = 'publicacion/lista_publicaciones.html'
    context_object_name = 'publicaciones'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all() 
        return context
    
    def get_queryset(self):
        queryset = Publicacion.objects.all()
        orden = self.request.GET.get('orden')

        # Validación de los valores de 'orden'
        if orden not in ['antiguas', 'alfabetico', 'recientes']:
            orden = 'recientes'

        if orden == 'antiguas':
            queryset = queryset.order_by('fecha_publicacion')
        elif orden == 'alfabetico':
            queryset = queryset.order_by('titulo_publicacion')
        else:
            queryset = queryset.order_by('-fecha_publicacion')
        
        return queryset


# Clase para mostrar todo el contenido del post

class DetallePublicacionView(DetailView):
    model = Publicacion
    template_name = 'publicacion/detalle_publicacion.html'
    context_object_name = 'publicacion'

    def post(self, request, *args, **kwargs):
        object = self.get_object()
        form = ComentarioForm(request.POST)
        print(form)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.publicacion = object
            comentario.autor = request.user
            print(comentario)
            comentario.save()
            return redirect('detalle_publicacion', pk=object.pk)
        return self.get_context_data(request, *args, **kwargs) 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm()
        return context

# Clase para Editar o modificar el post

class EditarPublicacionView(UserPassesTestMixin, UpdateView):
    model = Publicacion
    form_class = PublicacionForm
    template_name = 'publicacion/editar_publicacion.html'
    success_url = reverse_lazy('lista_publicaciones')
    
    def test_func(self):
        publicacion = self.get_object()
        return self.request.user == publicacion.usuario or self.request.user.is_superuser or self.request.user.is_staff


# Clase para borrar/eliminar el post

class BorrarPublicacionView(UserPassesTestMixin, DeleteView):
    model = Publicacion
    template_name = 'publicacion/eliminar_publicacion.html'
    success_url = reverse_lazy('lista_publicaciones')

    def test_func(self):
        publicacion = self.get_object()  
        # Permitir si el usuario es el autor del post, superuser o staff/colaborador
        return (self.request.user == publicacion.usuario or 
                self.request.user.is_superuser or 
                self.request.user.is_staff)

# Clase de lista de categoria

class ListaCategoriasView(UserPassesTestMixin, ListView):
    model = Categoria
    template_name = 'categorias/lista_categorias.html'
    context_object_name = 'categorias'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff or self.request.user.is_authenticated

# Clase de editar categoria

class EditarCategoriaView(UserPassesTestMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias/editar_categoria.html'
    success_url = reverse_lazy('lista_categorias')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff
    
#Para eliminar/borrar la categoria

class EliminarCategoriaView(UserPassesTestMixin, DeleteView):
    model = Categoria
    template_name = 'categorias/eliminar_categoria.html'
    success_url = reverse_lazy('lista_categorias')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff
    
    