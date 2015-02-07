from django.db import models
from django.contrib import admin


class ImageGallery(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True),
    base_name = models.CharField(max_length=50)
    image_count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    
    def images_list(self):
        result = []
        for x in range(0,image_count):
            if x < 10:
                url = base_name + "0" + str(x)
            else:
                url = base_name + str(x)
                
            result << url
        
        return result
            
    def thumbnails_list(self):
        result = []
        for x in range(0,image_count):
            if x < 10:
                url = base_name + "0" + str(x) + "t"
            else:
                url = base_name + str(x) + "t"
                
            result << url
        
        return result
    
    def  __str__(self):
        return self.base_name

#not sure if this works
class ImageGalleryAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["__str__", "title","image_count", "base_name", "created"]
    list_filter = ["base_name"]

# do i put this in the admin.py file?
admin.site.register(ImageGallery, ImageGalleryAdmin)