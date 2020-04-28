from django.urls import path
from . import views
urlpatterns=[
            path('',views.listings,name='listings'),
            path('<int:id>',views.listing,name='listing')
]
