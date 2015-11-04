from django.db import models
from django.contrib import admin
from phonenumber_field.modelfields import PhoneNumberField

class Service (models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    price = models.IntegerField()
    service_company_name = models.CharField(max_length=50)
    service_company_phone = PhoneNumberField()

    def __unicode__(self):
        return self.title

admin.site.register(Service)

