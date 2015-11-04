from django.db import models
from django.contrib import admin
from UserProfile.models import Person

class Guest(models.Model):
    first_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    car_id = models.CharField(max_length=15)

    def __unicode__(self):
        return self.last_name + ' ' + self.first_name


class GuestPass(models.Model):
    person = models.ForeignKey(Person)
    guest = models.ForeignKey(Guest)
    date = models.DateField()
    
    def __unicode__(self):
        return self.guest.last_name + ' ' + self.car_id

    class Meta:
        verbose_name_plural = 'Guest passes'
    
admin.site.register(Guest)
admin.site.register(GuestPass)
