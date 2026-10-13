from django.shortcuts import redirect, render
from .models import Feedback , Movie , Janr

# Create your views here.
def feed_back(requests):
    if requests.method == "POST":
        name = requests.POST.get("name","").strip
        message = requests.POST.get("message", "").strip()
        if name and message:
            Feedback.objects.create(name=name, message=message)
            return redirect("feedback")

def create_movie(requests):
    if requests.method == "POST":
        name = requests.POST.get("name","").strip
        description = requests.POST.get("description","").strip
        date_movie = requests.POST.get("date_movie", "").strip
        cover = requests.POST.get("cover","").strip
        Janr = requests.POST.get("Janr","").strip
        
        if name and description and date_movie and cover and Janr:
            Movie.objects.create(name=name, description=description, date_movie=date_movie, cover=cover,Janr= Janr)
            return redirect("movie")
        



        

    
    

