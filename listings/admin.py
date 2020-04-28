from django.contrib import admin
from .models import Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display=('id','title','realtor','listing_date')
    list_display_links=('title',)
    list_per_page=2
    search_fields=('title','zip')
    list_filter=('state','realtor')

admin.site.register(Listing,ListingAdmin)
