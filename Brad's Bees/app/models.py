from django.db import models

# Create your models here.

class Submission(models.Model):

    REMOVAL = "removal"
    POLLINATION = "pollination"
    EDUCATION = "education"
    HIVE_SETUP = "hive_setup"

    SERVICE_CHOICES = [
        (REMOVAL, "Bee Removal"),
        (POLLINATION, "Pollination Service"),
        (EDUCATION, "Education Service"),
        (HIVE_SETUP, "Hive Set-Up"),
    ]

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12)
    service = models.CharField(
        max_length=20,
        choices=SERVICE_CHOICES,
        default=REMOVAL
    )
    message = models.TextField(max_length=999999)
    


class SubmissionImage(models.Model):
    submission = models.ForeignKey(
        Submission,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to='submissions/photos/')