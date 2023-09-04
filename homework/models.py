from django.db import models
from django.utils import timezone

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

