from django.db import models

# Create your models here.
class Janr(models.Model):
    name = models.CharField( max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    date_movie = models.DateField()
    cover = models.ImageField(upload_to='covers/', null=True , blank=True)
    Janr = models.ForeignKey(Janr, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Feedback(models.Model):
    name = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name
    
    
 
