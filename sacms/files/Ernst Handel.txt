from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name = 'detail'),
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name = 'results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name = 'vote'),
	url(r'^upload', views.upload_file, name= 'upload_file'),
	url(r'^download', views.download, name = 'download'),
	url(r'^donwload/(.+)/$', views.download_file, name = 'download_file'),
]