from django.db import models

# Create your models here.
class Airport(models.Model):
     city=models.CharField(max_length=40)
     code=models.CharField(max_length=3)

     def __str__(self):
         return f"{self.city}({self.code})"

class Flight(models.Model):
    origin=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="departures")
    destination=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="ariving")
    duration=models.IntegerField()

    def flight_is_valid(self):
        return (self.origin!=self.destination) and (self.duration>0)

    def __str__(self):
         return f"{self.id}: {self.origin} to {self.destination} in {self.duration}"
class Passenger(models.Model):
    first=models.CharField(max_length=30)
    last=models.CharField(max_length=30)
    flights=models.ManyToManyField(Flight,blank=True,related_name="passengers")

    def __str__(self):
       return f"{self.first} {self.last}"
