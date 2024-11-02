from django.shortcuts import render



def home_page(request):
        return render(request, 'fourth_task/home_page.html')

def shop_page(request):
        products = ['Спиннинг "Argument" 10-35 гр', 'Катушка "Daiwa" 3000', 'Шнур "Elite" 1,5 PE']
        context = {'products': products}
        return render(request, 'fourth_task/shop_page.html', context)

def cart_page(request):
        return render(request, 'fourth_task/cart_page.html')
