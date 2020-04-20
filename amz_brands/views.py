from django.shortcuts import render, redirect
from .models import Brand
from .forms import BrandForm
from django.http import QueryDict
from .filter import BrandFilter


def index(request):
    latest_brand = Brand.objects.all()
    filter_brands = BrandFilter(request.GET, queryset=latest_brand)

    if request.method == 'POST':
        entries = QueryDict(request.POST['content'])
        for index, entry_id in enumerate(entries.getlist('entry[]')):
            entry = Brand.objects.get(id=entry_id)
            entry.order = index
            entry.save()

    context = {
        'latest_brand': 'latest_brand',
        'filter': filter_brands,
    }

    return render(request, 'pages/index.html', context)


def enroll(request):
    form = BrandForm()
    if request.method == 'POST':
        print('Printing POST', request.POST)
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'pages/enroll.html', context)


def reports(request):
    brands = Brand.objects.all()
    context = {
        'brands': brands
    }
    return render(request, 'pages/reports.html', context)


def account_details(request):
    return render(request, 'pages/account_details.html')
