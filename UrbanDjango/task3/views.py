from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'third_task/home_page.html'

class ShopPage(TemplateView):
    template_name = 'third_task/shop_page.html'

class CartPage(TemplateView):
    template_name = 'third_task/cart_page.html'