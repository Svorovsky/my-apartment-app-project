from django.db import models
from django.contrib import admin

"""
from django.core.files.images import ImageFile
from django.core.files import File


class DeliveryServiceLogo(ImageFile):
    logo = models.ImageField(width=200px, height=200px

class MenuFile(File):
    name = ()
"""

class DeliveryService(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='/Delivery/logos')
    menu_file = models.FileField(upload_to='/Delivery/menu_files')

    def __unicode__(self):
        return self.title

admin.site.register(DeliveryService)
