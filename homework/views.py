from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify

from homework.models import Product, Category, BlogPost
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


class BlogPostListView(ListView):
    model = BlogPost
    
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('homework:list')

    def form_valid(self, form):
        if form.is_valid():
            new_content = form.save()
            new_content.slug = slugify(new_content.title)
            new_content.save()

        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'content', 'preview', 'is_published')

    def form_valid(self, form):
        if form.is_valid():
            new_content = form.save()
            new_content.slug = slugify(new_content.title)
            new_content.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('homework:view', args=[self.kwargs.get('pk')])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'homework/blogpost_confirm_delete.html'
    success_url = reverse_lazy('homework:list')
