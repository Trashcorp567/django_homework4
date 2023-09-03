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


def product_detail(request, pk):
    category_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(pk=pk),
        'title': f'Товар - {category_item.name}'
    }
    return render(request, 'catalog/product_detail.html', context)
