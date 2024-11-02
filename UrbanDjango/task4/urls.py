from django.urls import path
from .views import home_page, shop_page, cart_page

urlpatterns = [
    path('', home_page),
    path('shop/', shop_page),
    path('cart/', cart_page),
]