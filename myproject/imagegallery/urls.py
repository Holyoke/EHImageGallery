from django.conf.urls import patterns, url

from imagegallery import views

urlpatterns = patterns('',
    # ex: /gallery/15_wildcostume
    url(r'/gallery/^(?P<base_name>)', views.thumbnails, name='thumbnails'),
    # ex: /gallery/15_wildcostume/01
    url(r'/gallery/^(?P<base_name>)/^(?P<question_id>\d+), views.image, name='image'),
    
    # ex: /polls/5/results/
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)