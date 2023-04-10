from django.shortcuts import render
from .models import Sovchi
# Create your views here.
from django.http import HttpResponse


def index(request):
    sovchi = Sovchi.objects.all()
    return render(request,'index.html',{'sovchi':sovchi})

def re_post(request):
    return HttpResponse("Nimadir post")