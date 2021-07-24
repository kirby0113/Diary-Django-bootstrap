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

def update(request):
    id = request.POST.get("id")
    diary = Diary.objects.filter(id=id).first()
    diary.title = request.POST.get("title",)
    diary.author = request.POST.get("author",)
    diary.content = request.POST.get("content",)
    date = datetime.date.today()
    diary.date = date
    try:
        image = request.FILES['image']
    except:
        pass
    else:
        diary.image = image
    finally:
        diary.save()
    return redirect("/")

def delete(request,id):
    diary = Diary.objects.filter(id=id).first()
    diary.delete()
    return redirect("/")