from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('api/upload/', views.upload_file, name='upload_file'),
]