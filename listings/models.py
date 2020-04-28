from django.db import models
from realtors.models import Realtor
from datetime import datetime
# Create your models here.
class Listing(models.Model):
    realtor=models.ForeignKey(Realtor,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField()
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip=models.CharField(max_length=20)
    sqrt=models.IntegerField()
    plot_size=models.DecimalField(max_digits=3,decimal_places=1)
    price=models.CharField(max_length=100)
    bedrooms=models.IntegerField()
    is_published=models.BooleanField(default=False)
    listing_date=models.DateTimeField(default=datetime.now)
    main_photo=models.ImageField(upload_to='image')
    optional_photo1=models.ImageField(upload_to='image',blank=True)
    optional_photo2=models.ImageField(upload_to='image',blank=True)
    optional_photo3=models.ImageField(upload_to='image',blank=True)
    optional_photo4=models.ImageField(upload_to='image',blank=True)
    optional_photo5=models.ImageField(upload_to='image',blank=True)
    optional_photo6=models.ImageField(upload_to='image',blank=True)
    def __str__(self):
        return self.title
