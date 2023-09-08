from django.shortcuts import render
from homework.models import Product, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.


class IndexView(ListView):
    model = Category
    template_name = 'homework/index.html'
    context_object_name = 'object_list'
    extra_context = {'title': 'Категории'}


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': "Категории товаров"
}


class ProductListView(ListView):
    model = Product
    template_name = 'homework/product_detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk,
        context_data['title'] = f'Категория - {category_item.name}'

        return context_data


def product_view(request, pk):
    category_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(pk=pk),
        'title': f'Товар - {category_item.name}'
    }
    return render(request, 'homework/product_view.html', context)
