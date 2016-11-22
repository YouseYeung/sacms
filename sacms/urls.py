from django.conf.urls import url

from . import views

urlpatterns = [
    # index page
    # ex: /sacms/
    url(r'^$', views.index, name='index'),
    # news feed page
    # ex: /sacms/news/
    url(r'^news/$', views.newsfeed, name='newsfeed'),
    # news article page
    # ex: /sacms/news/5/
    url(r'^news/(?P<article_id>[0-9]+)/', views.article, name='article'),
    # research group info page
    # ex: /sacms/groups/
    url(r'^groups/$', views.groups, name='groups'),
    # data analysis page
    # ex: /sacms/data/
    url(r'^data/$', views.data, name='data'),
]
