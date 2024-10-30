from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def func_repres(request):
    return render(request, 'second_task/func_repres.html')

class class_repres(TemplateView):
    template_name = 'second_task/class_repres.html'