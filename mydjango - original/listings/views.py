import imp
from django.shortcuts import render,redirect
from .models import Listing
from django.http import HttpResponse
from .form import ListingForm
# Create your views here.
def listings_list(request, ):

    listings = Listing.objects.all()

    context = {
         "listings":listings 
         
    }
    # return HttpResponse(request)
    return render(request,'listings.html',context)

def listings_retrieve(request,pk):
    # get specfic data using id 
    listing=Listing.objects.get(id=pk) 
    context = {

        "listing":listing

    }   
    # return HttpResponse(listings)
    return render(request,'listing.html',context)

def listing_create(request):
    form =ListingForm()

    #if form has data and is post method 
    if request.method == "POST":
        print(request.POST)
        form = ListingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/list')        
           

    context = {
    "form": form    
    }

    return render(request,'listing_create.html',context)


def listing_update(request,pk):
     # get specfic data using id 
    listings=Listing.objects.get(id=pk)
    form =ListingForm(instance=listings)



    #if form has data and is post method 
    if request.method == "POST":
        print(request.POST)
        form = ListingForm(request.POST, instance=listings)

        if form.is_valid():
            form.save()
            return redirect('/list')        
           

    context = {
    "form": form    
    }

    return render(request,'listing_update.html',context)    


def listing_delete(request,pk):
     # get specfic data using id 
    listings=Listing.objects.get(id=pk)
    listings.delete()
    return redirect('/list')  
