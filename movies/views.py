from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from .models import Movie, Janr, Feedback

def feedback(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        message = request.POST.get("message", "").strip()

        if name and message:
            Feedback.objects.create(
                name=name,
                message=message
            )
            return redirect("feedback")
    return render(request, "feedback.html")

def create_movie(request):
    janrs = Janr.objects.all()
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        description = request.POST.get("description", "").strip()
        date_movie = request.POST.get("date_movie")
        cover = request.FILES.get("cover")
        janr_id = request.POST.get("Janr")

        if name and description and date_movie and janr_id:
            janr = get_object_or_404(Janr, id=janr_id)

            Movie.objects.create(name=name,description=description,date_movie=date_movie,cover=cover,Janr=janr)
            return redirect("home")
    return render(request, "create.html", {
        "janrs": janrs
    })

def home(request):
    movies = Movie.objects.all()
    return render(request, "home.html", {
        "movies": movies
    })


def update_movie(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == "POST":
        movie.name = request.POST.get("name", movie.name)
        movie.description = request.POST.get("description", movie.description)
        movie.date_movie = request.POST.get("date_movie", movie.date_movie)
        janr_id = request.POST.get("Janr")

        if janr_id:
            movie.Janr = get_object_or_404(Janr,id=janr_id)
        cover = request.FILES.get("cover")
        if cover:
            movie.cover = cover
        movie.save()

        return redirect("home")

    return HttpResponseNotAllowed(["POST"])


def delete_movie(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == "POST":
        movie.delete()
        return redirect("home")
    return HttpResponseNotAllowed(["POST"])






        

    
    

