from django.conf.urls import url

from . import views

urlpatterns = [
    # index page
    # ex: /sacms/
    url(r'^$', views.index, name='index'),
    url(r'^en/$', views.index_en, name='index_en'),

    # news feed page (list of all news article titles)
    # ex: /sacms/news/
    url(r'^news/$', views.newsfeed, name='newsfeed'),
    url(r'^news/en/$', views.newsfeed_en, name='newsfeed_en'),    

    # news article page
    # ex: /sacms/news/5/
    url(r'^news/(?P<article_id>[0-9]+)/', views.article, name='article'),
    url(r'^news/(?P<article_id>[0-9]+)/en/', views.article_en, name='article_en'),

    # meetings page
    # ex: /sacms/meetings
    url(r'^meetings/$', views.meetings, name='meetings'),
    url(r'^meetings_en/$', views.meetings_en, name='meetings_en'),

    # meetings meeting page
    # ex: /sacms/meetings/5/
    url(r'^meetings/(?P<meeting_id>[0-9]+)/', views.meeting, name='meeting'),
    url(r'^meetings/(?P<meeting_id>[0-9]+)/en', views.meeting_en, name='meeting_en'),

    # all research groups in JSON
    # ex: /sacms/json/groups
    url(r'^json/groups', views.groups_json, name='groups_json'),

    # DEPRECATED
    # research group info page
    # ex: /sacms/groups/
    url(r'^groups/$', views.groups, name='groups'),
    url(r'^teams/$', views.groups_en, name='groups_en'),

    # research group in JSON
    # ex: /sacms/group/1/
    url(r'^json/group/(?P<group_id>[0-9]+)/', views.group, name='group'),

    # data analysis page
    # ex: /sacms/data/
    url(r'^data/$', views.data, name='data'),
    url(r'^data/en/$', views.data_en, name='data_en'),

    # show file's description
    # ex: /scams/description
    url(r'^decription/(?P<file_id>[0-9]+)/', views.description, name='description'),

    # upload file
    # ex: /sacms/upload
    url(r'^upload/$', views.upload, name= 'upload'),
    url(r'^upload/en/$', views.upload_en, name= 'upload_en'),
    url(r'^upload_file', views.upload_file, name= 'upload_file'),

    # download file
    # ex: /scams/download and /sacms/download/file_name
    url(r'^download', views.download, name = 'download'),
    url(r'^donwload/(.+)/$', views.download_file, name = 'download_file'),
]
