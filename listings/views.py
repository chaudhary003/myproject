from django.shortcuts import render,get_object_or_404
from .models import Listing
from django.core.paginator import Paginator
# Create your views here.
def listings(request):
    listings=Listing.objects.all()
    paginator=Paginator(listings,3)
    page=request.GET.get('page')
    listing_per_page=paginator.get_page(page)
    context={
    'listings':listing_per_page
    }
    return render(request,'listings/listings.html',context)
def listing(request,id):
    listing=get_object_or_404(Listing,pk=id)
    context={
    'listing':listing
    }

    return render(request,'listings/listing.html',context)
def listing_by_title(request,title):
    listing=get_object_or_404(Listing,title=title)
    context={
    'listing':listing
    }
    return render(request,'listings/listing.html',context)
