from django.shortcuts import render, HttpResponse, redirect
from .models import urlModel
import random

def home(request):
    return render(request, 'home.html')

def makeShortUrl(request):
    if request.method == "POST":
        longurl = request.POST['longurl']
        s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$*&^-+."
        shorturl=("".join(random.sample(s,6)))
        object = urlModel.objects.create(longurl=longurl, shorturl=shorturl)
        print("object created")
        shorturl = "http://127.0.0.1:8000/" + shorturl
    #return HttpResponse("Your short URL for {} is {}".format(longurl, shorturl))
    return render(request, "result.html", context={"shorturl":shorturl, "longurl":longurl})

def redirectUrl(request, shorturl):
    print(shorturl)
    try:
        obj = urlModel.objects.get(shorturl=shorturl)
    except urlModel.DoesNotExist:
        obj = None
    if obj is not None:
        print("Object Found")
        print(obj.longurl)
        obj.count += 1
        obj.save()
        return redirect(obj.longurl)
    else:
        return HttpResponse("Check your URL")
