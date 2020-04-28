from django.shortcuts import render
from listings.models import Listing
# Create your views here.
def home(request):
    latest_listings=Listing.objects.all()
    context={
    'latest_listings':latest_listings
    }
    return render(request,'pages/index.html',context)
def aboutus(request):
    return render(request, 'pages/about.html')
