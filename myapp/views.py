from django.shortcuts import render, HttpResponse
from .models import info
from .forms import ImageForm
from .models import image
import time
# Create your views here.
def index(request):
    if request.method == "POST":

        name= request.POST.get('name')
        subject= request.POST.get('subject')
        a= info(name=name, subject=subject)
        a.save()
    return render (request, "home.html")
    

def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    return render(request, "upload.html", {'form':form})
   



    

