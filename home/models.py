from django.db import models

# Create your models here.

class product(models.Model):
    imgname = models.CharField(max_length=225)
    price = models.FloatField()
    stock = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    descr = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.imgname