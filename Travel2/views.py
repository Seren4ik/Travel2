from django.shortcuts import render


def home(request):
    name = "Сергея"
    return render(request, "home.html", {'name': name})
