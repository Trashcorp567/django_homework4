from django.urls import path

from homework.apps import HomeworkConfig
from homework.views import IndexView, ProductListView, CategoryListView, product_view

app_name = HomeworkConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('<int:pk>/product_detail/', ProductListView.as_view(), name='product_detail'),
    path('<int:pk>/product_view/', product_view, name='product_view')
]
