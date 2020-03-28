from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Listing
from .choices import bedroom_choices,price_choices
# Create your views here.

def index(request):
	listings = Listing.objects.all()
	context={
	'listings':listings
	}
	return render(request,'listings/listings.html',context)

def listing(request,listing_id):
	listing = get_object_or_404(Listing,pk=listing_id)
	context={
	'listing':listing
	}
	return render(request,'listings/listing.html',context)

def search(request):
	queryset_list=Listing.objects.order_by('-list_date')
	#keywords
	if 'keywords' in request.GET:
		keywords=request.GET['keywords']#get the data from the searchbarko form
		if keywords:
			queryset_list=queryset_list.filter(description__icontains=keywords)#match and get data from the database
	if 'city' in request.GET:
		city=request.GET['city']
		if city:
			queryset_list=queryset_list.filter(city__iexact=city)

	if 'price' in request.GET:
		price=request.GET['price']
		if price:
			queryset_list=queryset_list.filter(price__lte=price)#less than or equals to

	if 'bedrooms' in request.GET:
		bedrooms=request.GET['bedrooms']
		if bedrooms:
			queryset_list=queryset_list.filter(bedroom__lte=bedrooms)#less than or equals to 


	context={
	'bedroom_choices':bedroom_choices,
	'price_choices':price_choices,
	'listings':queryset_list,
	'values':request.GET
	}
	return render(request,'listings/search.html',context)