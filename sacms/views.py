from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Article, ResearchGroup, Meeting
from django.http import HttpResponse, StreamingHttpResponse

import json
#os model用于获取文件路径
import os
#codecs model用于读取含中文字符的文件
import codecs

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
def meetings(request):
    """ Return the page for the list of all meetings """
    meeting_list = Meeting.objects.order_by('held_date')
    context = {'meeting_list': meeting_list}
    return render(request, 'sacms/meetings.html', context)

@login_required
def article(request, article_id):
    """ Return the page for a news article """
    article = get_object_or_404(Article, pk=article_id)
    context = {'article': article}
    return render(request, 'sacms/article.html', context)

@login_required
def meeting(request, meeting_id):
    """ Return the meeting for meetings_list """
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    context = {'meeting': meeting}
    return render(request, 'sacms/meeting.html', context)

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
    personnel = list()
    for p in group.personnel.all():
        personnel.append(p.username)
    resp['personnel'] = personnel
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

@login_required
def upload(request):
    return render(request, 'sacms/upload.html')

@login_required
def upload_file(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理  
        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None  
        if not myFile:  
            return HttpResponse("no files for upload!")
        filePath = os.getcwd() + "\\sacms\\files\\" + myFile.name #获取当前目录并保存上传的文件至当前目录
        destination = open(filePath,'wb+')    # 打开特定的文件进行二进制的写操作  
        for chunk in myFile.chunks():      # 分块写入文件  
            destination.write(chunk)
        destination.close()  
        return HttpResponse("upload over!")

@login_required
def download(request):
    fileDir = os.listdir(os.getcwd() + "\\sacms\\files\\")
    return render(request, 'sacms/download.html', {'fileDir': fileDir})

@login_required
def download_file(request, file_name):
    full_file_name = os.getcwd() + "\\sacms\\files\\" + file_name
    #分行下载分担服务器负担
    def file_iterator(file_name):
        #利用codecs model来使用Utf-8编码读取文件就不会出现中文乱码问题
        with codecs.open(file_name, 'r', 'utf-8') as f:
            lines = f.readlines()
            for l in lines:
                yield l

    the_file_name = full_file_name
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    #file_name若为utf-8的中文名，则需要转换成gb2312的编码方式才能显示出中文
    response['Content-Disposition'] = ('attachment; filename=' + file_name).encode('gb2312')
    return response