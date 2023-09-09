from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование категории')
    description = models.CharField(max_length=100, verbose_name='описание')
    create_date = models.DateField(**NULLABLE, verbose_name='дата добавления')

    def __str__(self):
        return f'{self.name} - {self.description}'

    class Meta:
        verbose_name = 'наименование категории'
        verbose_name_plural = 'наименование категорий'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название товара')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', default=1)
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='media/', verbose_name='превью', **NULLABLE)
    price = models.IntegerField(**NULLABLE, verbose_name='цена за покупку')
    create_date = models.DateField(**NULLABLE or timezone.now(), verbose_name='дата добавления')

    def __str__(self):
        return f'{self.name} - {self.description}: {self.category}'

    class Meta:
        verbose_name = 'название товара'
        verbose_name_plural = 'название товаров'


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, verbose_name='Slug')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog_previews/', verbose_name='Превью', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блоговая запись'
        verbose_name_plural = 'Блоговые записи'
