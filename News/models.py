from django.db import models
from django.contrib import admin
from django.core.files.images import ImageFile

class NewsItem(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50) 
    content = models.TextField()
    image = models.ImageField(upload_to='/News/images')

    def __unicode__(self):
        return self.title

admin.site.register(NewsItem)

