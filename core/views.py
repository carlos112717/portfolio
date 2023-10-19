from django.shortcuts import render, HttpResponse


# Creación de las vistas


def home(request):
    return render(request, 'core/home.html')


def aboutme(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')
