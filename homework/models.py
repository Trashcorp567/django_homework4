from django.db import models

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название товара')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='media/', verbose_name='превью', **NULLABLE)
    price = models.IntegerField(**NULLABLE, verbose_name='цена за покупку')

    def __str__(self):
        return f'{self.name}: {self.description}'

    class Meta:
        verbose_name = 'название товара'
        verbose_name_plural = 'название товаров'
