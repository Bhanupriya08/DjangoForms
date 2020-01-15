from django.db import models
from phone_field import PhoneField

# Create your models here.
class ContactUs(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100,unique=True)
    Mnumber = PhoneField(null=False,help_text='Contact phone number')
    Subject = models.CharField(max_length=50)
    Message = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.Email}"
   
    
