from django.db import models
from django.contrib import admin


class ImageGallery(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True),
    base_name = models.CharField(max_length=50)
    image_count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    image_names = compile_images();
    thumbnails = compile_images();
    
    def compile_images(self):
        for x in range(0,image_count):
            if x < 10:
                url = base_name + "0" + str(x) + ".jpg"
            else:
                url = base_name + str(x) + ".jpg"
                
            self.image_names.append(url)
            
    def compile_thumbnails(self):
        for x in range(0,image_count):
            if x < 10:
                url = base_name + "0" + str(x) + "t.jpg"
            else:
                url = base_name + str(x) + "t.jpg"
                
            self.thumbnails.append(url)
    
    def  __str__(self):
        return self.base_name
        
class ImageGalleryAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["__str__", "title","image_count", "base_name", "created"]
    list_filter = ["base_name"]

admin.site.register(ImageGallery, ImageGalleryAdmin)