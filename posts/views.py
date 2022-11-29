from django.http import HttpResponse
from django.shortcuts import render


def feed(request):
    # TODO: переписать
    return render(request, "base.html", context={"title": "Новости"})
