from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
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

            subject = "New Contact Form Submission"
            message = f"""

            You have received a new contact form submission.

            Name: {submission.name}
            Email: {submission.email}
            Message: {submission.message}

            """

            message += "\nAttached images:\n"
            for f in request.FILES.getlist('images'):
                message += f"- {f.name}\n"

            email = EmailMessage(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['bradbessetti@gmail.com'], # change to Brad's email
            )

            for f in request.FILES.getlist('images'):
                email.attach(f.name, f.read(), f.content_type)

            email.send()

            messages.success(request, "Form submitted successfully!")

            sub_count = Submission.objects.count()
            print(f"\nSUB COUNT: {sub_count}") # bash test for sub C func.

            image_count = SubmissionImage.objects.count()
            print(f"IMG COUNT: {image_count}\n") # bash test for img C func.

            return redirect('contact')
    
            
    else:
        form = SubmissionForm()

    return render(request, 'contact.html', {'form': form})



### FOR BRAD ###

# Step-by-step:
# Go to your Google account:
# https://myaccount.google.com/security

# Turn ON:
# 2-Step Verification (required)

# After that, go to:
# https://myaccount.google.com/apppasswords

# Create a new app password:
# App: Mail
# Device: Other → type "Django"

# Google will give you a 16-character password like:
# abcd efgh ijkl mnop



### FOR ME ###

# in settings.py:
# EMAIL_HOST_PASSWORD = 'abcdefghijklmnop'  # ← app password (NO spaces)