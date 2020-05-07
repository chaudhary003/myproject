from django.shortcuts import render
from listings.models import Listing
from listings.choices import state_choices,bedroom_choices,price_choices
# Create your views here.
def home(request):
    latest_listings=Listing.objects.all()
    context={
    'latest_listings':latest_listings,
    'state_choices':state_choices,
    'bedroom_choices':bedroom_choices,
    'price_choices':price_choices
    }
    return render(request,'pages/index.html',context)
def aboutus(request):
    return render(request, 'pages/about.html')
