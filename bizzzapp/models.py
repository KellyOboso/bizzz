from django.db import models

# Create your models here.

class Book(models.Model):
    departure = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    traveldate = models.DateTimeField(auto_now_add=True)
    buses = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.departure

class seats(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

class details(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.username

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.title





