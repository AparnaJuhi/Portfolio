from django.db import models
class Contact(models.Model):
    name=models.CharField(max_length=100)
    message=models.TextField()
    date=models.DateField()
# Create your models here.
