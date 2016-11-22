from django.shortcuts import get_object_or_404, render
from .models import Article, ResearchGroup
from django.contrib.auth.decorators import login_required
import json

def index(request):
    """ Return the home page """
    context = {'is_logged_in': request.user.is_authenticated}
    return render(request, 'sacms/index.html', context)

@login_required
def newsfeed(request):
    """ Return the page for the list of all news articles """
    article_list = Article.objects.order_by('published_date')
    context = {'article_list': article_list}
    return render(request, 'sacms/newsfeed.html', context)

@login_required
def article(request, article_id):
    """ Return the page for a news article """
    article = get_object_or_404(Article, pk=article_id)
    context = {'article': article}
    return render(request, 'sacms/article.html', context)


@login_required
def groups_json(request):
    """ Return the JSON of all research groups with name and id """
    resp = []
    group_list = ResearchGroup.objects.order_by('name')
    for group in group_list:
        resp.append({'name': group.name, 'id': group.id})
    return HttpResponse(json.dumps(resp, ensure_ascii=False), content_type="application/json; charset=utf-8")

@login_required
def groups(request):
    """ Deprecated: return the page of list of all research groups """
    group_list = ResearchGroup.objects.order_by('name')
    context = {'group_list': group_list}
    return render(request, 'sacms/groups.html', context)

@login_required
def group(request, group_id):
    """ Return the JSON object for a group with group_id as primary key """
    group = get_object_or_404(ResearchGroup, pk=group_id)
    resp = {}
    resp['name'] = group.name
    resp['personnel'] = group.personnel.split()
    resp['projects'] = group.projects.split()
    resp['papers'] = group.papers.split()
    # ensure_ascii set to False will ensure that Django won't
    # escape UTF-8 characters
    return HttpResponse(json.dumps(resp, ensure_ascii=False), content_type='application/json; charset=utf-8')

@login_required
def data(request):
    """ Return the data analysis page """
    context = {}
    return render(request, 'sacms/data.html', context)
