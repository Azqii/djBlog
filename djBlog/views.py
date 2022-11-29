from django.shortcuts import redirect, render


def index(request):
    if request.user.is_authenticated:
        return redirect("feed", permanent=True)
    return redirect("login", permanent=True)
