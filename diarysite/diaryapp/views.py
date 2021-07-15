from django.shortcuts import render
from .models import Diary

# Create your views here.

def index(request):
    DiaryList = Diary.objects.all()
    return render(request,"diaryapp/index.html",{"DiaryList":DiaryList})
