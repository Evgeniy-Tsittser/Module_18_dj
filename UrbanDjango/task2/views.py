from django.shortcuts import render

# Create your views here.

def func_repres(request):
    return render(request, 'second_task/func_repres.html')

def class_repres(request):
    return render(request, 'second_task/class_repres.html')