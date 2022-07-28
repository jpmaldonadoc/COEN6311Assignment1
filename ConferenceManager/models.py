from django.db import models

# Create your models here.
class attendee (models.Model):
    Name = models.CharField(max_length=30)
    Address = models.CharField(max_length=50)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    speaker = models.BooleanField()


class Event (models.Model):
    IDEvent = models.IntegerField()
    NameEvent = models.CharField(max_length=200)
    Description = models.CharField(max_length=500)
    Day = models.DateField()
    Time = models.DateTimeField()
    NameRoom = models.CharField(max_length=50)
    speaker = models.CharField(max_length=50)

class Room (models.Model):
    IDRoom = models.IntegerField()
    NameRoom = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    def __str__(self):
        return self.NameRoom




