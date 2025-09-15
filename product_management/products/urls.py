from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('api/upload/', views.upload_file, name='upload_file'),
    path('api/products/', views.product_list, name='product_list'),
]