from django.urls import path

from homework.apps import HomeworkConfig
from homework.views import index, product_detail, categories, product_view

app_name = HomeworkConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('<int:pk>/product_detail/', product_detail, name='product_detail'),
    path('<int:pk>/product_view/', product_view, name='product_view')
]
