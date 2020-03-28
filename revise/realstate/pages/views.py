from django.shortcuts import render
from django.http import HttpResponse
from realtors.models import Realtor
from listings.models import Listing
from listings.choices import bedroom_choices,price_choices

# Create your views here.
def index(request):
	listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
	context={
		'listings':listings,
		'bedroom_choices':bedroom_choices,
		'price_choices':price_choices

	}
	return render(request,'pages/index.html',context)

def about(request):
	realtors = Realtor.objects.all()
	mvp_realtors = Realtor.objects.filter(is_mvp=True)
	context={
		'realtors':realtors,
		'mvp_realtors':mvp_realtors
	}

	return render(request,'pages/about.html',context)