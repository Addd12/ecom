from django.shortcuts import render


def about(request):
    return render(request, "index/about.html")
