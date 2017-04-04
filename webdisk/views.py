#encoding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from webdisk.models import Files
import time
# Create your views here.
@csrf_exempt
def upload(req):
    if req.method == "GET":
        return render(req, 'upload.html')
    elif req.method == "POST":
        file_disc = req.POST['file_discribe']
        file_self = req.FILES.get('up_file',None)
        file_name = file_self.name
        file_size = file_self.size
        print(file_size)
        print(req.FILES)
        timenow =time.strftime("%Y%m%d%H%M%S")
        Files.objects.create(file_name=file_name, file_url="/files/"+file_name)
        return HttpResponse("<h1>接收成功<h1>")
