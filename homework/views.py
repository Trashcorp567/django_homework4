from django.shortcuts import render
from homework.models import Product
# Create your views here.


def index(request):
    context = {
        'object_list': Product.objects.all()[:3],
        'title': 'Пример товаров'
    }
    return render(request, 'catalog/index.html', context)


def full_list(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Все товары'
    }
    return render(request, 'catalog/full_list.html', context)

