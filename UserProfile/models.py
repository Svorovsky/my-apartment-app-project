from django.db import models
from django.contrib import admin 
from phonenumber_field.modelfields import PhoneNumberField

class Person(models.Model):
    phone_number = PhoneNumberField()
    first_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    apartment_number = models.CharField(max_length=5)
    car_id = models.CharField(max_length=12)
    def __unicode__(self):
        return self.last_name + ' ' + self.first_name

admin.site.register(Person)

