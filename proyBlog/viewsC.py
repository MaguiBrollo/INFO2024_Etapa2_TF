
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.core.mail import BadHeaderError
from smtplib import SMTPException
from django.conf import settings
from django.template.loader import render_to_string 

from .formsC import ContactanosForm

def contactanosView(request):
   error = None  # Variable para el mensaje de error
   if request.method == 'POST':
      form = ContactanosForm(request.POST)
      if form.is_valid():

         nombre = form.cleaned_data['nombre']
         correo = form.cleaned_data['correo']
         asunto = form.cleaned_data['asunto']
         mensaje = form.cleaned_data['mensaje']

         template = render_to_string('contactanosemail.html',{
              'nombre':nombre,
              'correo': correo,
              'asunto': asunto,
              'mensaje': mensaje
         })
         asuntomail = "Mensaje desde SIX BLOG"
         remitente = settings.EMAIL_HOST_USER
         destinatario = ['xx@gmail.com']

         try:
               email = EmailMessage(asuntomail, template, remitente, destinatario)
               email.send(fail_silently=False)
               
               return render(request, 'contactanosgracias.html')
         except BadHeaderError:
               error = "Encabezado inválido."
         except SMTPException as e:
               error = f"Error enviando el correo: {e}"
         except Exception as e:
               error = f"Ocurrió un error inesperado: {e}"
   else:
      form = ContactanosForm()

   return render(request, 'contactanos.html', {'form': form, 'error': error})
