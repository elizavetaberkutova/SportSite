from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def football(request):
    return render(request, 'football.html')


def hockey(request):
    return render(request, 'hockey.html')


def basketball(request):
    return render(request, 'basketball.html')