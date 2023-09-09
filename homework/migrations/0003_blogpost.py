# Generated by Django 4.2.5 on 2023-09-08 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0002_alter_category_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Slug')),
                ('content', models.TextField(verbose_name='Содержимое')),
                ('preview', models.ImageField(upload_to='blog_previews/', verbose_name='Превью')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликовано')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'Блоговая запись',
                'verbose_name_plural': 'Блоговые записи',
            },
        ),
    ]