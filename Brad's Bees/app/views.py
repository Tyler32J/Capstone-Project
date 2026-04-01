from django.shortcuts import render
import app.forms
import app.models


# Create your views here.
def admin_home(request):
    return render(request, "admin_home.html")


def bee_removal(request):
    return render(request, "bee_removal.html")

def render_ed_page(request):
    return render(request, "educational.html")


def render_gallery(request):
    return render(request, "gallery.html")



def render_home_page(request):
    return render(request, "home.html")



def render_index(request):
    return render(request, "index.html")


def shop(request):
    return render(request, "shop.html")