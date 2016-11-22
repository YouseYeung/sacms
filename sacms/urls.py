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
]
