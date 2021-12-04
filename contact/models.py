from django.db import models

# Create your models here.


class ContactInfo(models.Model):
    place = models.CharField(max_length=50)
    phone_number  = models.CharField(max_length=11)
    whatsapp  = models.CharField(max_length=11)
    email = models.EmailField(max_length=254)


    def __str__(self):
        return 'Contact Information'

