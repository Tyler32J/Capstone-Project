from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.

def contact_view(request):
    if request.method == "POST":
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save()

            files = request.FILES.getlist('images')
            for f in files:
                SubmissionImage.objects.create(
                    submission=submission,
                    image = f
                )

            sub_count = Submission.objects.count()
            print(f"\nSUB COUNT: {sub_count}") # bash test for sub C func.

            image_count = SubmissionImage.objects.count()
            print(f"IMG COUNT: {image_count}\n") # bash test for img C func.

    else:
        form = SubmissionForm()

    return render(request, 'contact.html', {'form': form})
