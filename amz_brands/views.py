from django.shortcuts import render, get_object_or_404
from .models import Brand
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def brand_details(request, brand_id):
    brand_details = get_object_or_404(Brand, pk=brand_id)
    context = {
        'brand_details': brand_details
    }
    return render(request, 'amz_brands/brand_details.html', context)
