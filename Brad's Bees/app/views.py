from django.shortcuts import render

# Create your views here.
def admin_home(request):
    return render("admin_home.html")



def bee_removal(request):
    return render("bee_removal.html")



def render_ed_page(request):
    return render("educational.html")



def render_gallery(request):
    return render("gallery.html")



def render_home_page(request):
    return render("home.html")



def render_index(request):
    return render("index.html")



def shop(request):
    return render("shop.html")