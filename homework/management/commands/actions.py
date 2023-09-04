from django.core.management.base import BaseCommand
from homework.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Удаляем старые данные
        Category.objects.all().delete()

        # Создаем новые данные
        category1 = Category.objects.create(name='Фото и видео', description='Объективы')
        category2 = Category.objects.create(name='Техника', description='Электронная техника')
