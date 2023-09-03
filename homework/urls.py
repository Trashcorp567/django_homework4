from django.urls import path

from homework.apps import HomeworkConfig
from homework.views import index, full_list, product_detail

app_name = HomeworkConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('full_list/', full_list, name='full_list'),
    path('product_detail/<int:pk>/', product_detail, name='product_detail'),
]
