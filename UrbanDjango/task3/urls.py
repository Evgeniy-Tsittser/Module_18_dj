from django.urls import path
from .views import HomePage, ShopPage, CartPage

urlpatterns = [
    path('', HomePage.as_view()),
    path('shop/', ShopPage.as_view()),
    path('cart/', CartPage.as_view()),
]