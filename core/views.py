from django.shortcuts import render


def index(request):
    context = {
        "title": "Welcome",
        "header": "Home Index"
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        "title": "About us",
        "header": "About us"
    }
    return render(request, 'index.html', context)


def contact(request):
    context = {
        "title": "Contact us",
        "header": "Contact us"
    }
    return render(request, 'index.html', context)
