from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'third_task/base.html')


def shop(request):
    products = [
        {"name": "Носки с оленями", "price": 150},
        {"name": "Свитер с мишкой", "price": 2500},
        {"name": "Лисий хвост", "price": 5000},
    ]
    return render(request, 'third_task/shop.html', {'products': products})


def cart(request):
    return render(request, 'third_task/cart.html')
