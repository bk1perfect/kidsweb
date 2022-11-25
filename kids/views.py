from django.shortcuts import render, HttpResponse
import random

def index(request):

    return render(request, 'index.html')

def color(request):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    context = {
    "colors" : str(f"rgb({r}, {g}, {b})")
    }

    return render(request, 'color.html', context)

def animal(request):
    
    context = {
    "num" : random.randint(1, 111)
    }
    return render(request, 'animal.html', context)