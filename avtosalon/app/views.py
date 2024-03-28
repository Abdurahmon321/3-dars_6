from django.shortcuts import render

# Create your views here.
from .models import Car, Category, Color


def home(request):
    return render(request, 'app/index.html')


def category_mashinalar(request, category_name):
    category = Category.objects.get(category=category_name)
    cars = Car.objects.filter(category=category)
    return render(request, 'app/mashinalar.html', {'category': category, 'cars': cars})


def filter_from_color(request, color_name):
    color = Color.objects.get(color=color_name)
    cars = Car.objects.filter(color=color)
    return render(request, 'app/mashinalar.html', {"color": color, "cars": cars})

def xizmatlar_page(request):
    return render(request, 'app/xizmatlar.html')


def category_page(request):
    categories = Category.objects.all()
    colors = Color.objects.all()
    return render(request, 'app/avto_modellar1.html', {"categories": categories, "colors": colors})
