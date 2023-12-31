from django.urls import path

from homework.apps import HomeworkConfig
from homework.views import IndexView, ProductListView, CategoryListView, product_view, BlogPostListView, \
    BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView

app_name = HomeworkConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('<int:pk>/product_detail/', ProductListView.as_view(), name='product_detail'),
    path('<int:pk>/product_view/', product_view, name='product_view'),
    path('create/', BlogPostCreateView.as_view(), name='create'),
    path('list/', BlogPostListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogPostDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogPostUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogPostDeleteView.as_view(), name='delete'),
]
