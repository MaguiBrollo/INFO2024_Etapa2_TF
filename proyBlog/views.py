from django.core.mail import EmailMessage
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .formsC import ContactanosForm


def index(request):
   context = {}
   return render(request,'index.html',context)    

class NosotrosView(TemplateView):
   template_name ='nosotros.html'
   success_url = reverse_lazy('index')

class BlogView(TemplateView):
   template_name ='blog.html'
   success_url = reverse_lazy('index')


#--------------- enviar mail
from django.core.mail import send_mail
from django.conf import settings

def contactanosView(request):
   if request.method == 'POST':
      formulario = ContactanosForm(request.POST)
      if formulario.is_valid():
         nombre = formulario.cleaned_data['nombre']
         correo = formulario.cleaned_data['correo']
         asunto = formulario.cleaned_data['asunto']
         mensaje = formulario.cleaned_data['mensaje']
         
         mensajeC =  "Usuario: {}\n Correo: {}\n \n Mensaje: {}\n\n".format(nombre,correo,mensaje)

         remitente = settings.EMAIL_HOST_USER
         destinatarios = ['maguieb@hotmail.com']
      
         try:
            send_mail(asunto, mensajeC, remitente, destinatarios)
            return redirect("/contactanos/?valido")
         except:
            return redirect("/contactanos/?novalido")
       
   else:
      formulario = ContactanosForm()
  
   context = {
      'form': formulario,
   }
   return render(request, 'contactanos.html', context)