from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'fourth_task/base.html')


def shop(request):
    context = {'products': ["Носки с оленями", "Свитер с мишкой", "Лисий хвост"]}
    return render(request, 'fourth_task/shop.html', context)


def cart(request):
    return render(request, 'fourth_task/cart.html')
