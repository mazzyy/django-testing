
# from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path , include
from listings.views import listings_list , listings_retrieve ,listing_create ,listing_update ,listing_delete
from playground.views import say_hello
from customer.views import index
# import playground

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', say_hello ),
    path('customer/',index),

    
    path('list/', listings_list ),
    path('retrieve/<pk>/', listings_retrieve ),
    path('retrieve/<pk>/edit', listing_update ),
       path('retrieve/<pk>/delete', listing_delete ),
    path('create/', listing_create ),
   


  
    # path('playground/', include('playlist.urls')),
    # path('list/',include('todo.urls')),
    
]
