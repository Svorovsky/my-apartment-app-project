from django.db import models
from django.contrib import admin

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50)
    apartment_number = models.CharField(max_length=5)
    def __unicode__(self):
        return self.last_name + ' ' + self.first_name
    
class Guest(models.Model):
    first_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.last_name + ' ' + self.first_name


class GuestPass(models.Model):
    person = models.ForeignKey(Person)
    guest = models.ForeignKey(Guest)
    car_id = models.CharField(max_length=12)
    date = models.DateField()
    def __unicode__(self):
        return self.guest.last_name + ' ' 
    class Meta:
        verbose_name_plural = 'Guest passes'
    

admin.site.register(Person)
admin.site.register(Guest)
admin.site.register(GuestPass)
