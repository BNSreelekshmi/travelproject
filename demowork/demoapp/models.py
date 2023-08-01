from django.db import models

# Create your models here.
class placedetail(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pictures')
    desc = models.TextField()

    def __str__(self):
        return self.name

class teamdetail(models.Model):
    pname = models.CharField(max_length=250)
    images = models.ImageField(upload_to='pictures')
    detail = models.TextField()

    def __str__(self):
        return self.pname
