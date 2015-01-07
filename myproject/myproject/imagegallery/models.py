from django.db import models
from django.contrib import admin


class ImageGallery(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True),
    base_name = models.CharField(max_length=50)
    image_count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    
    def  __str__(self):
        return self.base_name
        
class ImageGalleryAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["__str__", "title","image_count", "base_name", "created"]
    list_filter = ["base_name"]

admin.site.register(ImageGallery, ImageGalleryAdmin)