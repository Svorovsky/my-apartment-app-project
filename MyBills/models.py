from django.db import models
from django.contrib import admin
from UserProfile.models import Person
from phonenumber_field.modelfields import PhoneNumberField

class Bill(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=50)
    service_company_name = models.CharField(max_length=50)
    help_phone_number = PhoneNumberField()

    def __unicode__(self):
        return self.title + ' ' + '(' + self.service_company_name + ')'

class PersonalBill(models.Model):
    person = models.ForeignKey(Person)
    bill = models.ForeignKey(Bill)
    monthly_bill = models.CommaSeparatedIntegerField(max_length=12)
    arrear = models.CommaSeparatedIntegerField(max_length=12)

    def __unicode__(self):
        return self.person.last_name + ' ' + '(' + self.bill.title + ')'

admin.site.register(Bill)
admin.site.register(PersonalBill)


