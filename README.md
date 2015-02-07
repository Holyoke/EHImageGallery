# EHImageGallery

A Django app that scraped file names from a seperate server and produce views with thumbnails. 

What was unique about this implementation is that we have to read a certain file name format. 

The images were uploaded manually to another server, so Django's job was to create models which accepted a base name and a count of total images, which then generates the view.

