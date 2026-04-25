from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubmissionForm
from .models import Submission, SubmissionImage

# Create your views here.
def render_home_page(request):
    if request.method == "POST":
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save()

            SubmissionImage.objects.bulk_create([
                SubmissionImage(submission=submission, image=f)
                for f in request.FILES.getlist('images')
            ])

            messages.success(request, "Form submitted successfully!")
            return redirect('home')

    else:
        form = SubmissionForm()

    return render(request, "home.html", {"form": form})

def bee_removal(request):
    return render(request, "bee_removal.html")

def render_services_page(request):
    return render(request, "services.html")

def render_educational_page(request):
    return render(request, "educational.html")

def render_gallery(request):
    return render(request, "gallery.html")

def render_index(request):
    return render(request, "index.html")

