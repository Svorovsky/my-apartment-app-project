from django.db import models
from django.contrib import admin
from phonenumber_field.modelfields import PhoneNumberField

class InfoUnit(models.Model):
    title = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=150)

    def __unicode__(self):
        return self.title

admin.site.register(InfoUnit)


