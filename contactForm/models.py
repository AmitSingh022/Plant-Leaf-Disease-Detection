from django.db import models
from tinymce.models import HTMLField

class ContactForm(models.Model):
    image=models.FileField(upload_to="contactForm/",max_length=259,null=True)
    
# Create your models here.
