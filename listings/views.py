from django.shortcuts import render,get_object_or_404
from .models import Listing
# Create your views here.
def listings(request):
    return render(request,'listings/listings.html')
def listing(request,id):
    listing=get_object_or_404(Listing,pk=id)
    context={
    'listing':listing
    }
    return render(request,'listings/listing.html',context)
