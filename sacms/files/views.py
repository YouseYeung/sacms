from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Choice, Question

import os

#返回一个页面
'''
def index(request):
	return render(request, 'polls/index.html')
'''	
#返回交互式页面
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/form.html', context)	

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

	
def results(request, question_id):
	response = "results of question %s"
	return HttpResponse(response %question_id)
	
# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
	
def upload_file(request):  
    if request.method == "POST":    # 请求方法为POST时，进行处理  
        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None  
        if not myFile:  
            return HttpResponse("no files for upload!")
        filePath = os.getcwd() + "\\polls\\files\\" + myFile.name #获取当前目录并保存上传的文件至当前目录
        destination = open(filePath,'wb+')    # 打开特定的文件进行二进制的写操作  
        for chunk in myFile.chunks():      # 分块写入文件  
            destination.write(chunk)  
        destination.close()  
        return HttpResponse("upload over!")

def download(request):
    fileDir = os.listdir(os.getcwd() + "\\polls\\files\\")
    return render(request, 'polls/download.html', {'fileDir': fileDir})

def download_file(request, file_name):
    file_download = os.getcwd() + "\\polls\\files\\" + file_name #获取当前目录并保存上传的文件至当前目录
    return HttpResponse(file_download)
    with open(file_download) as f:
        c = f.read()  
    return HttpResponse(c)
