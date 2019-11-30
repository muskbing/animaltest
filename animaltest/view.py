from django.http import HttpResponse
from django.http import JsonResponse
import os
from django.conf import settings
import sys
from animalAPI import animalAPI

APP_ID ='17896377'
API_KEY ='Fi71Yp0B0ivGB8SNj9BFdi0b'
SECRET_KEY ='lwgXKw5suGRK3dYFnlSaRvVTWOoAIGES'

def index(request):
    return HttpResponse("Hello,This is felix's homepage!")

def hello(request):
    return HttpResponse("Hello,This is Fliex's website!")

def animalapi(request):
    print(request)
    name=""
    code=""
    if request.method=='GET':
        name=request.GET.get("name")
        code=request.GET.get("code")

    if request.method=='POST':
        name=request.POST.get("name")
        code=request.POST.get("code")
    print(name,code)
    return JsonResponse({"code":0,"message":"OK"})

def imgAPI(request):
    image=request.FILES['image']
    name='-'.join(image.name.split('.')[:-1])
    print(settings.BASE_DIR,settings.MEDIA_ROOT)
    fname= settings.BASE_DIR+settings.MEDIA_ROOT+name+'.jpg'
    fname=fname.replace("\\","/")
    print(fname)
    #先存储结果
    with open(fname,'wb') as pic:
        for c in image.chunks():
            pic.write(c)
    #开始访问API
    api=animalAPI(APP_ID,API_KEY,SECRET_KEY)
    try:
        res=api.query_api(fname)
        print(res)
        return JsonResponse({"res":res,"message":"OK"})
    except:
        return JsonResponse({"message":"Not OK"})


def getImage(request):
    imagepath = settings.BASE_DIR+settings.MEDIA_ROOT
    image_data = open(imagepath+'1.jpg', "rb").read()
    return HttpResponse(image_data, content_type="image/png")