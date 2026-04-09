from django.shortcuts import render, redirect
from django.core.mail import send_mail
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

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [business@example.com], # change to Brad's email
                fail_silently = False,
            )

            messages.success(request, "Form submitted successfully!")

            sub_count = Submission.objects.count()
            print(f"\nSUB COUNT: {sub_count}") # bash test for sub C func.

            image_count = SubmissionImage.objects.count()
            print(f"IMG COUNT: {image_count}\n") # bash test for img C func.

            return redirect('contact')
    
            
    else:
        form = SubmissionForm()

    return render(request, 'contact.html', {'form': form})

#### FOLLOWING IS EMAIL SETUP TEMPLATE FOR LAUNCH == SETTINGS.PY ####

#  EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#  EMAIL_HOST = 'smtp.gmail.com'
#  EMAIL_PORT = 587
#  EMAIL_USE_TLS = True
#  EMAIL_HOST_USER = 'your_email@gmail.com'
#  EMAIL_HOST_PASSWORD = 'your_app_password'
#  DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
