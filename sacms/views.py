from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Article, ResearchGroup, Meeting, myFile, Notice
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

def index_en(request):
    """ Return the home page """
    context = {'is_logged_in': request.user.is_authenticated}
    return render(request, 'sacms/index_en.html', context)

@login_required
def newsfeed(request):
    """ Return the page for the list of all news articles """
    article_list = Article.objects.order_by('published_date')
    context = {'article_list': article_list}
    return render(request, 'sacms/newsfeed.html', context)

@login_required
def newsfeed_en(request):
    """ Return the page for the list of all news articles """
    article_list = Article.objects.order_by('published_date')
    context = {'article_list': article_list}
    return render(request, 'sacms/newsfeed_en.html', context)

@login_required
def meetings(request):
    """ Return the page for the list of all meetings """
    meeting_list = Meeting.objects.order_by('held_date')
    context = {'meeting_list': meeting_list}
    return render(request, 'sacms/meetings.html', context)

@login_required
def meetings_en(request):
    """ Return the page for the list of all meetings """
    meeting_list = Meeting.objects.order_by('held_date')
    context = {'meeting_list': meeting_list}
    return render(request, 'sacms/meetings_en.html', context)

@login_required
def notices(request):
    """ Return the page for the list of all notices """
    notice_list = Notice.objects.order_by('published_date')
    context = {'notice_list': notice_list}
    return render(request, 'sacms/notices.html', context)

@login_required
def notice(request, notice_id):
    """ Return the page for a notice """
    notice = get_object_or_404(Notice, pk=notice_id)
    context = {'notice': notice}
    return render(request, 'sacms/notice.html', context)

@login_required
def notices_en(request):
    """ Return the page for the list of all notices """
    notice_list = Notice.objects.order_by('published_date')
    context = {'notice_list': notice_list}
    return render(request, 'sacms/notices_en.html', context)

@login_required
def notice_en(request, notice_id):
    """ Return the page for a notice """
    notice = get_object_or_404(Notice, pk=notice_id)
    context = {'notice': notice}
    return render(request, 'sacms/notice_en.html', context)

@login_required
def article(request, article_id):
    """ Return the page for a news article """
    article = get_object_or_404(Article, pk=article_id)
    context = {'article': article}
    return render(request, 'sacms/article.html', context)

@login_required
def article_en(request, article_id):
    """ Return the page for a news article """
    article = get_object_or_404(Article, pk=article_id)
    context = {'article': article}
    return render(request, 'sacms/article_en.html', context)

@login_required
def meeting(request, meeting_id):
    """ Return the meeting for meetings_list """
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    context = {'meeting': meeting}
    return render(request, 'sacms/meeting.html', context)

@login_required
def meeting_en(request, meeting_id):
    """ Return the meeting for meetings_list """
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    context = {'meeting': meeting}
    return render(request, 'sacms/meeting_en.html', context)

@login_required
def groups_json(request):
    """ Return the JSON of all research groups with name and id """
    resp = []
    group_list = ResearchGroup.objects.order_by('name')
    for group in group_list:
        resp.append({'name': group.name, 'id': group.id})
    return HttpResponse(json.dumps(resp, ensure_ascii=False), content_type="application/json; charset=utf-8")

@login_required

def groups(request, group_id = 1):
    """ return the page of list of all research groups
        and the info for the chosen group
    """
    group = get_object_or_404(ResearchGroup, pk=group_id)
    groups = ResearchGroup.objects.order_by('name')
    group_list = []
    for g in groups:
        if g.id is not group.id:
            group_list.append({'name': g.name, 'id': g.id})
    # default showing group
    # chosen group info
    group_info = {}
    group_info['name'] = group.name
    personnel = list()
    for p in group.personnel.all():
        personnel.append(p.username)
    group_info['personnel'] = " ".join(str(x) for x in personnel)
    group_info['projects'] = group.projects
    group_info['directions'] = group.directions
    group_info['papers'] = group.papers.split()
    context = {'group_list': group_list, 'group_info': group_info}
    return render(request, 'sacms/groups.html', context)

@login_required
def groups_en(request, group_id = 1):
    """ return the page of list of all research groups
        and the info for the chosen group
    """
    group = get_object_or_404(ResearchGroup, pk=group_id)
    groups = ResearchGroup.objects.order_by('name')
    group_list = []
    for g in groups:
        if g.id is not group.id:
            group_list.append({'name': g.name, 'id': g.id})
    # default showing group
    # chosen group info
    group_info = {}
    group_info['name'] = group.name
    personnel = list()
    for p in group.personnel.all():
        personnel.append(p.username)
    group_info['personnel'] = " ".join(str(x) for x in personnel)
    group_info['projects'] = group.projects
    group_info['directions'] = group.directions
    group_info['papers'] = group.papers.split()
    context = {'group_list': group_list, 'group_info': group_info}
    return render(request, 'sacms/groups_en.html', context)

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
    files = myFile.objects.order_by('name')
    context = {'files' : files}
    return render(request, 'sacms/data.html', context)

@login_required
def data_en(request):
    """ Return the data analysis page """
    files = myFile.objects.order_by('name')
    context = {'files' : files}
    return render(request, 'sacms/data_en.html', context)

@login_required
def upload(request):
    return render(request, 'sacms/upload.html')

@login_required
def upload_en(request):
    return render(request, 'sacms/upload_en.html')

@login_required
def upload_file(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        #request.POST是一个字典对象，可以用['attributename']来获取相应的属性值
        file_name = request.POST['file_name']
        file_team = request.POST['file_team']
        file_country = request.POST['file_country']
        file_description = request.POST['file_description']
        #往数据库中加入新增的文件描述数据
        addFile = myFile.objects.create(name = file_name, team = file_team, country = file_country, description = file_description)
        addFile.save()
        myfile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myfile:
            return HttpResponse("no files for upload!")
        filePath = os.getcwd() + "\\sacms\\files\\" + myfile.name #获取当前目录并保存上传的文件至当前目录
        destination = open(filePath,'wb+')    # 打开特定的文件进行二进制的写操作
        for chunk in myfile.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()
        return HttpResponse("upload over!")

@login_required
def download(request):
    fileDir = os.listdir(os.getcwd() + "\\sacms\\files\\")
    return render(request, 'sacms/download.html', {'fileDir': fileDir})

@login_required
def description(request, file_id):
    theDescription = get_object_or_404(myFile, pk = file_id)
    return HttpResponse(theDescription.description)

@login_required
def download_file(request, file_name):
    full_file_name = os.getcwd() + "\\sacms\\files\\" + file_name
    #分行下载分担服务器负担
    def file_iterator(file_name):
        d = file_name.split('.')
        if d[1] == 'txt':
            with codecs.open(file_name, 'r', 'gb2312') as f:
                lines = f.readlines()
                for l in lines:
                    yield l
        else:
            with codecs.open(file_name, 'r', 'utf-8') as f:
                lines = f.readlines()
                for l in lines:
                    yield l
        f.close()

    the_file_name = full_file_name
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    #file_name若为utf-8的中文名，则需要转换成gb2312的编码方式才能显示出中文
    response['Content-Disposition'] = ('attachment; filename=' + file_name).encode('gb2312')
    return response
