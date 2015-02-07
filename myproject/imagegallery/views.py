from django.shortcuts import render
from django.http import HttpResponse

from imagegallery.models import ImageGallery

#gallery view
def index(request):
    ctx = {}
    return render(request, 'image.html', ctx)


    