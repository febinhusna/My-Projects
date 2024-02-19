from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class Men(models.Model):
    name_men=models.CharField(max_length=250)
    img_men=models.ImageField(upload_to='pics')
    desc_men=models.TextField()

    def __str__(self):
        return self.name_men
