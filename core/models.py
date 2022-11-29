from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.pk} | {self.name} | {self.email}"


class Workshop(models.Model):
    subject = models.CharField(max_length=255)
    description = models.TextField()
    on_going = models.BooleanField()
    insta_link = models.URLField()
    workshop_link = models.URLField()
