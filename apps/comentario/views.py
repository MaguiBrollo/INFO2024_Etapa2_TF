from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .models import Publicacion, Comentario
from .forms import ComentarioForm
from django.utils import timezone
from django.contrib.auth.mixins import UserPassesTestMixin

class DetallePublicacionView(DetailView):
    model = Publicacion
    template_name = 'publicacion/detalle_publicacion.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm()
        return context

    def post(self, request, *arg, **kwargs):
        self.object = self.get_object()
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.publicacion = self.object
            comentario.autor = request.user
            comentario.fecha_creacion = timezone.now()
            comentario.save()
            return redirect('detalle_publicacion', pk=self.object.pk)
        return self.render_to_response(self.get_context_data(form=form))

class EditarComentarioView(UserPassesTestMixin, UpdateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'editar_comentario.html'
    success_url = reverse_lazy('lista_publicaciones')

    def test_func(self):
        comentario = self.get_object()
        return self.request.user == comentario.autor or self.request.user.is_superuser or self.request.user.is_staff
  
    def form_valid(self, form):
        form.instance.edited = True
        form.instance.fecha_modificacion = timezone.now()
        return super().form_valid(form)

#  @login_required 
#     def editar_comentario(request, pk):
#         comentario = get_object_or_404(Comentario, pk=pk, autor=request.user)
#         if request.mehtod == 'POST':
#             form = ComentarioForm(request.POST, isinstance=comentario)
#             if form.is_valid():
#                 form.save()
#                 return redirect('detalle_publicacion', pk=comentario.publicacion.pk)
        
#         else:
#             form = ComentarioForm(isinstance=comentario)
#         return render(request, 'comentario/editar_comentario.html', {'form': form})