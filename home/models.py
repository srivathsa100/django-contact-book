from django.db import models

# Create your models here.
class Contact(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    Email=models.EmailField()
    ContactNumber=models.CharField(max_length=10)
    picture = models.ImageField(upload_to='contact_pictures/', null=True, blank=True)
