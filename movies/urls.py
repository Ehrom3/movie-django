from django.urls import path
from . import views


urlpatterns = [
    path("", views.home,name="home"),
    path("create/", views.create_movie, name="create_movie"),
    path("update/<int:id>/",views.update_movie,name="update_movie"),
    path("delete/<int:id>/",views.delete_movie,name="delete_movie"),
    path("feedback/",views.feedback, name="feedback" ),

]