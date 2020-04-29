from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Data
 
# получение данных из бд
def index(request):
    data = Data.objects.all()
    return render(request, "reviews.html", {"data": data})
 
# сохранение данных в бд
def create(request):
    if request.method == "POST":
        data = Data()
        data.date = request.POST.get("date")
        data.car = request.POST.get("car")
        data.number = request.POST.get("number")
        data.comment = request.POST.get("comment")
        data.rating = request.POST.get("rating")
        data.save()
    return HttpResponseRedirect("/reviews/")

# изменение данных в бд
def edit(request, id):
    try:
        data = Data.objects.get(id=id)
 
        if request.method == "POST":
            data.date = request.POST.get("date")
            data.car = request.POST.get("car")
            data.number = request.POST.get("number")
            data.comment = request.POST.get("comment")
            data.rating = request.POST.get("rating")
            data.save()
            return HttpResponseRedirect("/reviews/")
        else:
            return render(request, "edit.html", {"data": data})
    except Data.DoesNotExist:
        return HttpResponseNotFound("<h2>Review not found</h2>")
     
# удаление данных из бд
def delete(request, id):
    try:
        data = Data.objects.get(id=id)
        data.delete()
        return HttpResponseRedirect("/reviews/")
    except Data.DoesNotExist:
        return HttpResponseNotFound("<h2>Review not found</h2>")


#def index(request):
 #   return render(request,'reviews/Head.html')


