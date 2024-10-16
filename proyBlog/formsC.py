from django import forms

class ContactanosForm(forms.Form):
   nombre = forms.CharField()
   correo = forms.EmailField()
   asunto = forms.CharField()
   mensaje=forms.CharField(widget=forms.Textarea, required=True)

   def __init__(self, *args, **kwargs):
      super(ContactanosForm, self).__init__(*args, **kwargs)

      self.fields['nombre'].widget.attrs['class'] = 'form-control'
      self.fields['nombre'].widget.attrs['placeholder'] = 'Nombre'

      self.fields['correo'].widget.attrs['class'] = 'form-control'
      self.fields['correo'].widget.attrs['placeholder'] = 'Correo electrónico'

      self.fields['asunto'].widget.attrs['class'] = 'form-control'
      self.fields['asunto'].widget.attrs['placeholder'] = 'Asunto'

      self.fields['mensaje'].widget.attrs['class'] = 'form-control'
      self.fields['mensaje'].widget.attrs['placeholder'] = 'Mensaje'
   
