# Generated by Django 4.2.5 on 2023-09-08 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0003_blogpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='blog_previews/', verbose_name='Превью'),
        ),
    ]
