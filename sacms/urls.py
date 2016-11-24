from django.conf.urls import url

from . import views

urlpatterns = [
    # index page
    # ex: /sacms/
    url(r'^$', views.index, name='index'),

    # news feed page (list of all news article titles)
    # ex: /sacms/news/
    url(r'^news/$', views.newsfeed, name='newsfeed'),

    # news article page
    # ex: /sacms/news/5/
    url(r'^news/(?P<article_id>[0-9]+)/', views.article, name='article'),

    # meetings page
    # ex: /sacms/meetings
    url(r'^meetings/$', views.meetings, name='meetings'),

    # meetings meeting page
    # ex: /sacms/meetings/5/
    url(r'^meetings/(?P<meeting_id>[0-9]+)/', views.meeting, name='meeting'),

    # all research groups in JSON
    # ex: /sacms/json/groups
    url(r'^json/groups', views.groups_json, name='groups_json'),

    # DEPRECATED
    # research group info page
    # ex: /sacms/groups/
    url(r'^groups/$', views.groups, name='groups'),

    # research group in JSON
    # ex: /sacms/group/1/
    url(r'^json/group/(?P<group_id>[0-9]+)/', views.group, name='group'),

    # data analysis page
    # ex: /sacms/data/
    url(r'^data/$', views.data, name='data'),

    # upload file
    # ex: /sacms/upload
    url(r'^file', views.upload, name= 'upload'),
    url(r'^upload_file', views.upload_file, name= 'upload_file'),
    
    # download file
    # ex: /scams/download and /sacms/download/file_name
    url(r'^download', views.download, name = 'download'),
    url(r'^donwload/(.+)/$', views.download_file, name = 'download_file'),
]
