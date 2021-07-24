from django.shortcuts import render,redirect
from .models import Diary
import datetime
# Create your views here.

def index(request):
    if request.method == "POST":
        title = request.POST.get("title",)
        author = request.POST.get("author",)
        content = request.POST.get("content",)
        image = request.FILES["image"]
        date = datetime.date.today()

        diary = Diary(title=title,author=author,content=content,date=date,image=image)
        diary.save()
        return redirect("/")
    DiaryList = Diary.objects.all()
    return render(request,"diaryapp/index.html",{"DiaryList":DiaryList})

def detail(request,id):
    diary = Diary.objects.get(id=id)
    return render(request,"diaryapp/detail.html",{"diary":diary})
