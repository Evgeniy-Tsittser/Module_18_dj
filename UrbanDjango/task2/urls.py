from django.urls import path
from . import views
from .views import func_repres, class_repres

urlpatterns = [
    path('func/', func_repres),
    path('class/', class_repres),
]