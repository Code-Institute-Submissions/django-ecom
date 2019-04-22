from django.shortcuts import render


def index(request):
    return render(request, "index.html", {'title': 'Home'})


def about(request):
    return render(request, 'about.html', {'title': 'About'})


def contact(request):
    return render(request, 'contact.html', {'title': 'Contact'})
