from django.views.generic import TemplateView
from django.shortcuts import render
from django.urls import reverse_lazy


def index(request):
   context = {}
   return render(request,'index.html',context)    

class NosotrosView(TemplateView):
   template_name ='nosotros.html'
   success_url = reverse_lazy('index')

class BlogView(TemplateView):
   template_name ='blog.html'
   success_url = reverse_lazy('index')
