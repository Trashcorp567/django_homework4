from django.shortcuts import render
from homework.models import Product, Category
from django.views.generic import ListView
# Create your views here.


def index(request):
    context = {
        'object_list': Category.objects.all()[:3],
        'title': 'Категории'
    }
    return render(request, 'homework/index.html', context)


def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Все категории'
    }
    return render(request, 'homework/categories.html', context)


def product_detail(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Категория - {category_item.name}'
    }
    return render(request, 'homework/product_detail.html', context)


def product_view(request, pk):
    category_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(pk=pk),
        'title': f'Товар - {category_item.name}'
    }
    return render(request, 'homework/product_view.html', context)
