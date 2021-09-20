from django.db import models

# Create your models here.

class Decade(models.Model):
    start_year = models.CharField(max_length=10000)
    def __str__(self):
        return str(self.year)

class Fad(models.Model):
    name = models.CharField(max_length=10000)
    image_url = models.CharField(max_length=10000)
    description = models.CharField(max_length=10000)
    decade = models.ForeignKey(Decade,on_delete=models.CASCADE, related_name="decades")
    def __str__(self):
        return str(self.name)