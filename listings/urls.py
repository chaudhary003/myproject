from django.urls import path
from . import views
urlpatterns=[
            path('',views.listings,name='listings'),
            path('<int:id>',views.listing,name='listing'),
            path('<title>',views.listing_by_title,name='listing_by_title'),
            path('search/',views.search,name='search')
]
