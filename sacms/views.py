from django.shortcuts import get_object_or_404, render
from .models import Article
from django.contrib.auth.decorators import login_required

def index(request):
    context = {'is_logged_in': request.user.is_authenticated}
    return render(request, 'sacms/index.html', context)

@login_required
def newsfeed(request):
    article_list = Article.objects.order_by('published_date')
    context = {'article_list': article_list}
    return render(request, 'sacms/newsfeed.html', context)

@login_required
def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {'article': article}
    return render(request, 'sacms/article.html', context)

@login_required
def groups(request):
    context = {}
    return render(request, 'sacms/groups.html', context)

@login_required
def data(request):
    context = {}
    return render(request, 'sacms/data.html', context)
