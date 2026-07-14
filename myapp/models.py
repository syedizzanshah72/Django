from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=500)
    message = models.TextField(max_length=1000)
    date = models.DateField()

    def __str__(self):
        return self.name
