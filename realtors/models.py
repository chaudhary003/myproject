from django.db import models

# Create your models here.
class Realtor(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    contact=models.CharField(max_length=100)
    display_pic=models.ImageField(upload_to='image')

    def __str__(self):
        return self.first_name+ ' '+ self.last_name
