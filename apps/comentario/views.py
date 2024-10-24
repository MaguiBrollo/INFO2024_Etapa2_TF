from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from .models import Publicacion, Comentario
from .forms import ComentarioForm
from django.utils import timezone


# Create your views here.
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