from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Listing
from django.core.paginator import Paginator


# Create your views here.
def index(request, ):
    # listings = Listing.objects.all()
    listing = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listing, 1)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # CITY
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # PRICE
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price_lte=price)

    context = {
        'listings': queryset_list,
    }
    return render(request, 'listings/search.html', context)
