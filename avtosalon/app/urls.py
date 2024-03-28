from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('avto_modellar/', views.category_page),
    path('xizmatlar/', views.xizmatlar_page),
    path('avto_modellar/<str:category_name>/', views.category_mashinalar, name='category_mashinalar'),
    path('avto_modellar/car_color/<str:color_name>/', views.filter_from_color, name='filter_from_color'),
]
